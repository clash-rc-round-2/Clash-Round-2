#!/bin/bash
y=1
g++ test_generator.cpp
while [ $y -lt 6 ]
do
	./a.out > input$y.txt
	y=$((y+1))
done
y=1
g++ user.cpp
while [ $y -lt 6 ]
do
	time ./a.out < input$y.txt >expected_output$y.txt
	y=$((y+1))
done