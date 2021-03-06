# Assignment 3 Part 1
Snehal Ranjan (2020121003)
VJS Pranavasri (2020121001)

## Values used
Rollnumber : 2020121001
x = 0.88
y = 2

Actions = Left, Right  
P(Success of action) = x = 0.88  
P(Failure of action) = 1-x = 0.12  

The follwing is the table used.  
|P(Observation/State)|O=Red|O=Green|
|--------------------|-----|-------|
|State=Red|0.9|0.1|
|State=Green|0.15|0.85|


![image](https://user-images.githubusercontent.com/17949836/115052410-8b8a2b00-9efb-11eb-8662-25e78addcf59.png)  
Belief states = [1/3, 0, 1/3, 0, 0, 1/3]  
As initially it is said to be on red.

## Action 1
Belief states B = [1/3, 0, 1/3, 0, 0, 1/3]  
*Agent took the action Right and observed Green.*  
  
Ub'[S1]=0.1[ (0.12 * 0.3333) + (0.12 * 0) + (0 * 0.3333) + (0 * 0) + (0 * 0) + (0 * 0.3333)]=0.0039996  
  
Ub'[S2]=0.85[ (0.88 * 0.3333) + (0 * 0) + (0.12 * 0.3333) + (0 * 0) + (0 * 0) + (0 * 0.3333)]=0.283305  
  
Ub'[S3]=0.1[ (0 * 0.3333) + (0.88 * 0) + (0 * 0.3333) + (0.12 * 0) + (0 * 0) + (0 * 0.3333)]=0.0  
  
Ub'[S4]=0.85[ (0 * 0.3333) + (0 * 0) + (0.88 * 0.3333) + (0 * 0) + (0.12 * 0) + (0 * 0.3333)]=0.2493084    
  
Ub'[S5]=0.85[ (0 * 0.3333) + (0 * 0) + (0 * 0.3333) + (0.88 * 0) + (0 * 0) + (0.12 * 0.3333)]=0.033996599999999995  
  
Ub'[S6]=0.1[ (0 * 0.3333) + (0 * 0) + (0 * 0.3333) + (0 * 0) + (0.88 * 0) + (0.88 * 0.3333)]=0.029330400000000003  
  
sum = sum(Ub') = 0.59994  
new B = [Ub'[Si]/sum for i in 1 to 6]  
  
B = [0.006666666666666666, 0.47222222222222215, 0.0, 0.41555555555555557, 0.05666666666666666, 0.04888888888888889]  

## Action 2
B = [0.006666666666666666, 0.47222222222222215, 0.0, 0.41555555555555557, 0.05666666666666666, 0.04888888888888889]  
*Agent took the action Left and observed Red.*  
  
Ub'[S1]=0.9[ (0.88 * 0.00666667) + (0.88 * 0.47222222) + (0 * 0.0) + (0 * 0.41555556) + (0 * 0.05666667) + (0 * 0.04888889)]=0.37928000088  
  
Ub'[S2]=0.15[ (0.12 * 0.00666667) + (0 * 0.47222222) + (0.88 * 0.0) + (0 * 0.41555556) + (0 * 0.05666667) + (0 * 0.04888889)]=0.00012000006000000001  
  
Ub'[S3]=0.9[ (0 * 0.00666667) + (0.12 * 0.47222222) + (0 * 0.0) + (0.88 * 0.41555556) + (0 * 0.05666667) + (0 * 0.04888889)]=0.38012000328  
  
Ub'[S4]=0.15[ (0 * 0.00666667) + (0 * 0.47222222) + (0.12 * 0.0) + (0 * 0.41555556) + (0.88 * 0.05666667) + (0 * 0.04888889)]=0.0074800004400000005  
  
Ub'[S5]=0.15[ (0 * 0.00666667) + (0 * 0.47222222) + (0 * 0.0) + (0.12 * 0.41555556) + (0 * 0.05666667) + (0.88 * 0.04888889)]=0.01393333356  
  
Ub'[S6]=0.9[ (0 * 0.00666667) + (0 * 0.47222222) + (0 * 0.0) + (0 * 0.41555556) + (0.12 * 0.05666667) + (0.12 * 0.04888889)]=0.011400000479999998  
  
sum = sum(Ub') =  0.7923333387000001  
new B = [Ub'[Si]/sum for i in 1 to 6]  
  
B = [0.4786874189874348, 0.00015145148403939045, 0.4797475818746587, 0.009440471673541609, 0.017585191584719568, 0.014387884395605828]  

## Action 3
B = [0.4786874189874348, 0.00015145148403939045, 0.4797475818746587, 0.009440471673541609, 0.017585191584719568, 0.014387884395605828]  
*Agent took the action Left and observed Green.*  
  
Ub'[S1]=0.1[ (0.88 * 0.47868742) + (0.88 * 0.00015145) + (0 * 0.47974758) + (0 * 0.00944047) + (0 * 0.01758519) + (0 * 0.01438788)]=0.042137820560000004  
  
Ub'[S2]=0.85[ (0.12 * 0.47868742) + (0 * 0.00015145) + (0.88 * 0.47974758) + (0 * 0.00944047) + (0 * 0.01758519) + (0 * 0.01438788)]=0.40767730667999996  
  
Ub'[S3]=0.1[ (0 * 0.47868742) + (0.12 * 0.00015145) + (0 * 0.47974758) + (0.88 * 0.00944047) + (0 * 0.01758519) + (0 * 0.01438788)]=0.0008325787599999999  
  
Ub'[S4]=0.85[ (0 * 0.47868742) + (0 * 0.00015145) + (0.12 * 0.47974758) + (0 * 0.00944047) + (0.88 * 0.01758519) + (0 * 0.01438788)]=0.06208797528  
  
Ub'[S5]=0.85[ (0 * 0.47868742) + (0 * 0.00015145) + (0 * 0.47974758) + (0.12 * 0.00944047) + (0 * 0.01758519) + (0.88 * 0.01438788)]=0.011725062179999999  
  
Ub'[S6]=0.1[ (0 * 0.47868742) + (0 * 0.00015145) + (0 * 0.47974758) + (0 * 0.00944047) + (0.12 * 0.01758519) + (0.12 * 0.01438788)]=0.00038367684  
  
sum = sum(Ub') = 0.5248444202999999  
new B = [Ub'[Si]/sum for i in 1 to 6]  
  
B = [0.08028630758028088, 0.776758389556609, 0.0015863344027247156, 0.11829786671736102, 0.02234007207945162, 0.0007310296635728568]  


## Final Results
Now we have the beliefs at the end of each action (Displayed upto only 4 digits for convinience)
* **Initial**  
  B = [0.3333, 0, 0.3333, 0, 0, 0.3333]  
* **Action 1**  
  B = [0.0066, 0.4722, 0.0, 0.4155, 0.0566, 0.0488]  
* **Action 2**  
  B = [0.4786, 0.0001, 0.4797, 0.0094, 0.0175, 0.0143]
* **Action 3 (Final Beliefs)**  
  B = [0.0802, 0.7767, 0.0015, 0.1182, 0.0223, 0.0007]
