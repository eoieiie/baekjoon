# [Silver IV] 괄호 - 9012 

[문제 링크](https://www.acmicpc.net/problem/9012) 

### 성능 요약

메모리: 32544 KB, 시간: 32 ms

### 분류

자료 구조, 문자열, 스택

### 제출 일자

2025년 6월 19일 23:05:12

### 문제 설명

<p>Parenthesis String (PS) consists of two parenthesis symbols ‘(’ and ‘)’ only. In parenthesis strings, some strings are called a valid PS (shortly, VPS). Let us give the formal definition of VPS. A single “( )” is a member of VPS, called the base VPS. Let x and y be a member of VPS. Then “(x)”, a VPS which encloses a VPS x with a single pair of parenthesis, is also a member of VPS. And xy, the concatenation of two VPS x and y, is a member of VPS. For example, “(())()” and ((()))” are all VPS, but “(()(”, “(())()))” and “(()” are not VPS. You are given a set of PS. You should decide if the input string is VPS or not. </p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Then PS’s are given in the following T lines one by one. The length of each PS is between 2 and 50, inclusively.</p>

### 출력 

 <p>Your program is to write to standard output. Print the result in each line. If the input string is a VPS, then print “YES”. Otherwise print “NO”. </p>

