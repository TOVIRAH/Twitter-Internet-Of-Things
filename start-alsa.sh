#!/usr/bin/env bash
echo $1; echo $2;
pkill arecord; arecord -D plughw:0,0 $1.$2.m1.wav & arecord -D plughw:1,0 $1.$2.m2.wav