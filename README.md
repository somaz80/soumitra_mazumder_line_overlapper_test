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
<pre>   line_1 = [-2, -6] <br/>
        line_2 = [-17, -11] <br/>
        are_line_segments_overlapping(line_1, line_2)</br>
        </pre>
