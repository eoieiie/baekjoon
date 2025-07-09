# [Bronze I] 유레카 이론 - 10448 

[문제 링크](https://www.acmicpc.net/problem/10448) 

### 성능 요약

메모리: 32412 KB, 시간: 148 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2025년 7월 9일 17:27:29

### 문제 설명

<p>A triangle number T<sub>n</sub>(n ≥ 1) is a figurate number that can be represented by a regular geometric arrangement of equally spaced points as illustrated in Figure 1.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/eureka.png" style="height:119px; width:416px"></p>

<p>Figure 1.</p>

<p>The triangle number T<sub>n</sub> for any positive integer n ≥ 1 is given by the explicit formula:</p>

<p>T<sub>n</sub> = 1 + 2 + 3 + ... + n = n(n+1)/2</p>

<p>In 1796, Gauss proved that every positive integer can be represented as a sum of at most three triangle numbers. For examples,</p>

<ul>
	<li>4 = T<sub>1</sub> + T<sub>2</sub></li>
	<li>5 = T<sub>1</sub> + T<sub>1</sub> + T<sub>2</sub></li>
	<li>6 = T<sub>2</sub> + T<sub>2</sub> or 6 = T<sub>3</sub></li>
	<li>10 = T<sub>1</sub> + T<sub>2</sub> + T<sub>3</sub> or 10 = T<sub>4</sub></li>
</ul>

<p>This result is known as the Eureka theorem since he wrote in his diary “Eureka! num = Δ + Δ + Δ” for commemorating the proof. We wonder if some positive integer can be represented as a sum of exactly three triangle numbers. As shown in the above examples, integers 5 and 10 can be represented as a sum of exactly three triangle numbers, but integers 4 and 6 cannot.</p>

<p>Given a positive integer, write a program to test whether or not the integer can be represented as a sum of exactly three triangle numbers that may not be distinct.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case consists of a line containing a positive integer K (3 ≤ K ≤ 1,000).</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for each test case. Print 1 if the input number K can be represented as a sum of exactly three triangle numbers, and print 0 (zero), otherwise.</p>

