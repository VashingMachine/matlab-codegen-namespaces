### Matlab to C++ Namespace adder
##### Description
The program adds namespace clauses in .cpp and .h files.  
Executing this program is needed for each exported Matlab function.
##### Usage
* --namespace &lt;name&gt; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pass name of namespace. Required.
* --dir &lt;path&gt; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Select folder with the exported function. If this argument is omitted, current directory is selected
##### Example
<code>matcppnamespaces --namespace ltpn --dir ./ltp</code>