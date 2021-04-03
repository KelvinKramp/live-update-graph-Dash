# live-update-graph-Dash

This code is supposed to solve the reload webpage problem if you use the Dash code. This problem occurs as a
consequence of the data being created in the callback. It causes the data to update at every webpage load. 
If your placing your Dash live-update graph online and your callback is retrieving  extra information at 
every callback then if multiple people to acces it or you try to access it on multiple computers 
this will cause you app to shift into the future... :-D. It sounds funny, but its not anymore if you 
have tried to find the problem for a couple of houres... 

For the wonderfull sentdex explanation of creating live update graphs in Dash see:
https://www.youtube.com/watch?v=37Zj955LFT0

For the explanation by the Dash team of the solution to this problem see:
https://community.plotly.com/t/solved-updating-server-side-app-data-on-a-schedule/6612

I havent been coding for a long time so sorry for all the elaborate extra information within the code
but it helps me structure my code. 
