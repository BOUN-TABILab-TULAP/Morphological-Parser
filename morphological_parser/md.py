#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random
from collections import defaultdict

MODEL_RE = re.compile(r"([^\s]*)\s+(.*)")
FEAT_SEP_RE = re.compile(r"([\+\-][^\[\]]+\[)")
avgw = defaultdict(int)

def disamb(amb_text,addAll):
    """
    amb_test: str
    """
    words = []
    all_parses = []
    result = ""
    lines = [line for line in amb_text.split("\n") if line]
    for line in lines:
        if (("<DOC>" in line) or ("</DOC>" in line) or 
                ("<TITLE>" in line) or ("</TITLE>" in line)):
            result += line + "\n";
            continue
        if "</S>" in line:
            best_score, best_parse_arr = best_parse(all_parses)
            for i, word in enumerate(words):
                result += "{} {}".format(word, best_parse_arr[i])
                if addAll:
                    parses = re.split(r"\s+", all_parses[i])
                    for parse in parses:
                        if parse != best_parse_arr[i]:
                            result += " {}".format(parse)
                result += "\n"
            result += "{}\n".format(line);
            words = []
            all_parses = []
            continue

        word, *parses = re.split(r"\s+", line)
        words.append(word)
        all_parses.append(" ".join(parses))

    return result

def best_parse(all_parses):
    all_parses.append("</s>")
    bestpath = defaultdict(str)
    states = defaultdict(int)
    states["<s> <s>"] = 0
    bestpath[0] = "-1 0 null"
    best_state_num = 0
    n = 0
    for parse in all_parses:
        best_score = -100000
        next_states = dict()
        cands = re.split(r"\s+", parse)
        random.shuffle(cands)
        for cand in cands:
            for state in states.keys():
                state_num = states[state]
                prev, score, parse = re.split(r"\s+", bestpath[state_num])
                score = float(score)
                prev = float(prev)
                hist = re.split(r"\s+", state)
                trigram = [hist[0], hist[1], cand]
                feat = defaultdict(int)
                extract_trigram_feat(feat, trigram)
                trigram_score = ascore(feat)
                new_score = score + trigram_score
                new_state = "{} {}".format(hist[1], cand)
                if new_state not in next_states:
                    n += 1
                    next_states[new_state] = n
                next_state_num = next_states[new_state]
                if next_state_num in bestpath:
                    _, cur_score, _ = re.split(r"\s+", bestpath[next_state_num])
                    cur_score = float(cur_score)
                    if new_score > cur_score:
                        bestpath[next_state_num] = "{} {} {}".format(state_num, new_score, cand)

                else:
                    bestpath[next_state_num] = "{} {} {}".format(state_num ,new_score ,cand)

                if new_score > best_score:
                    best_score = new_score
                    best_state_num = next_state_num
        states = next_states

    best_parse_arr = []
    state_num = best_state_num
    while state_num != 0:
        prev, score, parse = re.split(r"\s+", bestpath[state_num])
        prev = float(prev)
        best_parse_arr.insert(0, parse)
        state_num = prev

    best_parse_arr.pop()
    return [best_score, best_parse_arr]

def extract_trigram_feat(feat_dict, trigram):
    """
    trigram is list
    """
    w1, w2, w3 = trigram
    
    trigram[0] = FEAT_SEP_RE.sub(r" \1", trigram[0])
    r1, *IG1_arr = re.split(r"\s", trigram[0])
    IG1 = "".join(IG1_arr)

    trigram[1] = FEAT_SEP_RE.sub(r" \1", trigram[1])
    r2, *IG2_arr = re.split(r"\s", trigram[1])
    IG2 = "".join(IG2_arr)

    trigram[2] = FEAT_SEP_RE.sub(r" \1", trigram[2])
    r3, *IG3_arr = re.split(r"\s", trigram[2])
    IG3 = "".join(IG3_arr)

    feat_dict["1:{} {} {}".format(w1, w2, w3)] += 1
    feat_dict["2:{} {}".format(w1, w3)] += 1
    feat_dict["3:{} {}".format(w2, w3)] += 1
    feat_dict["4:{}".format(w3)] += 1
    feat_dict["5:{} {}".format(w2, IG3)] += 1
    feat_dict["6:{} {}".format(w1, IG3)] += 1
    feat_dict["7:{} {} {}".format(r1, r2, r3)] += 1
    feat_dict["8:{} {}".format(r1, r3)] += 1
    feat_dict["9:{} {}".format(r2, r3)] += 1
    feat_dict["10:{}".format(r3)] += 1
    feat_dict["11:{} {} {}".format(IG1, IG2, IG3)] += 1
    feat_dict["12:{} {}".format(IG1, IG3)] += 1
    feat_dict["13:{} {}".format(IG2, IG3)] += 1
    feat_dict["14:{}".format(IG3)] += 1

    for ig in IG3_arr:
        feat_dict["15:{}".format(ig)] += 1

    for i, ig in enumerate(IG3_arr):
        feat_dict["16:{} {}".format(i, ig)] += 1

    feat_dict["17:{}".format(len(IG3_arr))] += 1


def ascore(feat_dict):
    global avgw
    score = 0
    for feat in feat_dict.keys():
        score += avgw[feat] * feat_dict[feat]
    return score

def load_model(fname):
    global avgw
    with open(fname, "r") as f:
        lines = [line for line in f.read().split("\n") if line]
    
    for line in lines:
        weight, feat = MODEL_RE.split(line)[1:3]
        avgw[feat] = float(weight)


def init(fname):
    load_model(fname)
