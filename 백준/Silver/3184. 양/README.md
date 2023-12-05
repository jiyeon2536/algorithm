# [Silver I] 양 - 3184 

[문제 링크](https://www.acmicpc.net/problem/3184) 

### 성능 요약

메모리: 111620 KB, 시간: 156 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2023년 12월 5일 19:59:46

### 문제 설명

<p>There is certain number of sheep in Mickey's backyard. While he was firmly sleeping, hungry wolves came in the yard and attacked the sheep.</p>

<p>Yard is of rectangular shape and consists of fields arranged in rows and columns. Character '.' (dot) denotes an empty field, character '#' denotes a fence, character 'o' denotes a sheep and character 'v' denotes a wolf.</p>

<p>We consider that two fields are in the same region if we can move from one field to the other by a path consisting of horizontal and vertical moves only and not containing any fences. Fields from which we can "escape" from the yard are not considered to be a part of any region.</p>

<p>Fortunately, our sheep know karate – they can fight the wolves within a region and win (i.e. kill wolves) if their number in that region is greater than number of wolves in the same region. Otherwise, wolves eat all the sheep inside that region.</p>

<p>In the beginning, all the sheep and wolves are situated inside regions in the yard.</p>

<p>Write a program that will calculate the number of sheep and the number of wolves still alive in the morning. </p>

### 입력 

 <p>First line of input contains two integers, R i C, 3 ≤ R, C ≤ 250, the number of rows and the number of columns of Mickey's yard.</p>

<p>Each of the following R lines contains C characters. All of them together represent the layout of the yard i.e. positions of the fences, sheep and wolves in the yard.</p>

<p>Note: 50% of given test data will be "simple" in the sense that the inside area of every region will be of rectangular shape, and within that rectangle there will be no other fences. </p>

### 출력 

 <p>First and only line of output should contain two numbers, number of sheep and number of wolves still alive in the morning. </p>

