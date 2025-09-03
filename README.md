# TV Rating Engine

A simple Python tool that scores and ranks TVs based on price, screen size, and panel type.

## What It Does

This script takes in basic TV specs like price, inches, and screen type and returns a score and tier (A, B, or C). The results are sorted automatically so you can compare TVs side by side.

It uses basic Python structures like functions, lists, sorting with lambdas, and conditional logic.

## Features

- Scores based on:
  - Price range
  - Screen size
  - Panel type
- Outputs a clean comparison list
- Sorts TVs automatically by score

## Example Output
📊 TVs sorted by score:
- tcl: rating: A, score: 5
- lg: rating: B, score: 3
- sony: rating: B, score: 2
- samsung: rating: C, score: -1
