# Line Overlapping Problem </br>
<br/>
<b>Problem:</b><br/>
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis 
and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
<br/>
<b>Solution:</b><br/>
<b>are_line_segments_overlapping(line1, line2)</b</pre>
<p>Is the function that does the calulation and returns True if line segments overlap, 
returns False if the lines dont overalp. If supplied input is invalid then raises error.</p>
</br>
<p> In order to do this compare first it determines which line is existing on the left part of the axis and 
based on that it does the compare using regular arithmetic operator.</p>
<br/>
<b>Usage:</b>
<pre>line_1 = [-2, -6] <br/>
     line_2 = [-17, -11] <br/>
      are_line_segments_overlapping(line_1, line_2)</br>
        </pre> </br>
  <b>Test Cases:</b><br/>
  This function tested based on the following test cases:</br>
  <u>1> If two lines overlaps  on x axis  positive side. Both lines are on positive side of x axis.</br>
  2> If two lines overlaps on x axis negetive side. Both lines are on negative side of x axis.</br>
  3> If two lines does not overlap on positive side of x axis. Both lines are on positive side of x axis.</br>
  4> If two lines does not overlap on negative side of x axis. </br>In this case one line exist on positive side of xaxis and  another one in negative side of x axis.</br>
  5> If two lines does not overlap on both belonging to negative side of x axis.</br></u>
  
