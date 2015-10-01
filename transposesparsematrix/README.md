# Transpose table into a sparse matrix

`transposesparsematrix.py` is an answer I wrote as a solution to [this StackOverflow question](http://stackoverflow.com/q/32897249/2744166).

## Usage
```
python transposesparsematrix.py >> results.tsv
```

## Output
```
	day1	day2	day3	day4	day5	day6	day7	day8	day9	day10	day11	day12	day13	day14	day15	day16	day17	day18	day19	day20	day21	day22	day23	day24	day25	day26	day27	day28	day29	day30	day31	day32	day33	day34	day35	day36	day37	day38	day39	day40	day41	day42	day43	day44	day45	day46	day47	day48	day49	day50	day51	day52	day53	day54	day55	day56	day57	day58	day59	day60	day61	day62	day63	day64	day65	day66	day67	day68	day69	day70	day71	day72	day73	day74	day75	day76	day77	day78	day79	day80	day81	day82	day83	day84	day85	day86	day87	day88	day89	day90
x_time	10	10	9	0	0	0	0	0	0	0	0	0	0	0	2	7	0	10	0	0	0	0	0	0	3	0	0	0	0	0	5	0	0	0	2	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
g_up	0	0	0	8	3	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	3	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
t_msg	4	0	0	0	3	0	0	0	5	8	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	4

```

## Contents of the StackOverflow question:

### [Reshaping a table in python](http://stackoverflow.com/q/32897249/2744166)

Being new to Python I am finding it a little difficult to comprehend solutions to problems of 'similar' (not sure though) nature posted on the forum and all my attempts to correlate them with mine have not been successful

I have a .csv file (part of which) shown below

```
Rank Day Parameter
10	1	x_time
10	2	x_time
9	3	x_time
2	15	x_time
7	16	x_time
10	18	x_time
3	25	x_time
5	31	x_time
2	35	x_time
4	1	t_msg
3	5	t_msg
5	9	t_msg
8	10	t_msg
4	90	t_msg
8   4    g_up
3   5    g_up
3   56   g_up
```

Problem Statement: The .csv file has been extracted from a dataset; the aim of which is to study the pattern of the "parameter" over a span of period (say 90 days) along with its "rank"(gravity) on any given "day" of a period. The said parameter may or may not occur on a particular day during the said period.

A model now exists where every instance of occurrence of a parameter is being put in a separate row (of the csv file). What I am now attempting (in vain,till) is that for every unique parameter only one row may exist with 90 corresponding columns for each day(as the analysis window is 90 days). For all days when the parameter is ranked, its ranking comes in column as it is and the others are left as 0.

If may explanation has aided confusion let me put it in this way. Considering the csv file had been as shown could I reshape this to a one having 3 rows and 90 columns

```
              day1   day2   day3    day4  ............ day90 
    x_time     10     10    9        0                   0 
    t_msg       4      0    0        0                   4
    g_up        0      0    0        8                   0
```

PS:I understand that I have been mentioning .csv file all throughout but have put 'table' in the title as I'm made to believe that such a feat may only be accomplished through a table. Please correct me if wrong.

Thanking in anticipation 

-- Posted by [sherinkapotein](http://stackoverflow.com/users/613976/sherinkapotein)


