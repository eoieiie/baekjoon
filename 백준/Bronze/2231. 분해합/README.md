# [Bronze II] 분해합 - 2231 

[문제 링크](https://www.acmicpc.net/problem/2231) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 7월 7일 16:50:07

### 문제 설명

<p>For a positive integer N, the digit-sum of N is defined as the sum of N itself and its digits. When M is the digitsum of N, we call N a generator of M.</p>

<p>For example, the digit-sum of 245 is 256 (= 245 + 2 + 4 + 5). Therefore, 245 is a generator of 256.</p>

<p>Not surprisingly, some numbers do not have any generators and some numbers have more than one generator. For example, the generators of 216 are 198 and 207.</p>

<p>You are to write a program to find the smallest generator of the given integer.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case takes one line containing an integer N, 1 ≤ N ≤ 100,000.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for each test case. The line is to contain a generator of N for each test case. If N has multiple generators, print the smallest. If N does not have any generators, print 0.</p>

