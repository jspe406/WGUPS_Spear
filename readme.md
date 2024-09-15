## Scenario:
This task is the implementation phase of the WGUPS Routing Program.
<p> 
The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their daily local deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements that are listed in the attached “WGUPS Package File.”

Your task is to determine an algorithm, write code, and present a solution where all 40 packages will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.

The supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.
</p>

## Assumptions:
- Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
- The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
- There are no collisions.
- Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
- Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
- The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages to a truck at the hub). This time is factored into the calculation of the average speed of the trucks.
- There is up to one special note associated with a package.
- The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.
- The distances provided in the “WGUPS Distance Table” are equal regardless of the direction traveled.
- The day ends when all 40 packages have been delivered.

## Requirents:

### A. Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table

### B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:
![Screenshot 2024-09-14 224532.png](screenshots%2FScreenshot%202024-09-14%20224532.png)
### C.  Write an original program that will deliver all packages and meet all requirements using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and “WGUPS Package File.”

<br>
<center>
<img src="screenshots/Screenshot 2024-09-14 224830.png" style="width:75%">
</center>
<br>

### D.  Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any package at any time and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
***
### Check at 9:00 AM
<br>
<center>
<img src="screenshots/Screenshot 2024-09-14 221411.png" style="width:50%">
</center>
<br>

***

### Check at 10:00 AM
<br>
<center>
<img src="screenshots/Screenshot 2024-09-14 221450.png" style="width:50%">
</center>
<br>

***

### Check at 12:30 PM
<br>
<center>
<img src="screenshots/Screenshot 2024-09-14 221525.png" style="width:50%">
</center>
<br>

***

### E.  Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.
![Screenshot 2024-09-14 224924.png](screenshots%2FScreenshot%202024-09-14%20224924.png)
### F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:
1.  Describe two or more strengths of the algorithm used in the solution.
```
Two strengths from my algorithm are that it searches through all packages on the truck. Finds the closest package for each one assigned to the truck
then compares the best from each package and chooses the best option to add to the truck. Then it will repeat the same process with the all packages on the truck,
including the newly added until all spaces on truck are filled. Secondly it readjusts, if a package is manually added to the truck the algorithm can still run through
the list and find the most optimal route.
```

2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
```
3. All checks have been completed to meet all system requirements. All packages are delivered to the correct address, ontime and completed all the special notes.
``` 

4. Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.
```
The Dijkstra algorithm and the Nearest neighbor algorithm
```
-  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.
```
The Dijkstra is used to find optimal ways on weighted paths. Our paths are not weighted based on time. We are only concerned with the mileage.
The nearest neighbor algorithm is also a good option and similar to what I chose but differs in the way that it would choose the closest package regardless of if that package can be delivered at that given time or on a specific truck. My alogrithm will compare all closest elements for
package on the truck and choose whichever is the best option at the given time based on the special notes and available packages.
```

### G.  Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.
```
If I were to attempt this again I would love to spend more time building out a more intuitive GUI that could present filters instead of just running query functions in the terminal
```

### H.  Verify that the data structure used in the solution meets all requirements in the scenario.
```
All data requirements have been checked and verified. Hash Table is a clean and efficient way to store the data for the packages.
```

1.  Identify two other data structures that could meet the same requirements in the scenario.
```
Graph Nodes or a linked list would have also completed the task necessary to hold the data.
```

- Describe how each data structure identified in H1 is different from the data structure used in the solution.
```
Graph nodes and linked lists are node-based structures which means they use pointers, while hash tables use an array-based structure with a hash function which is very useful.
A graph node could be used to store data on the distances and addresses well so that you could implement a breadth or depth first aproach
A linked list would be useful to hold the information but to hold the same data as the hash table, it would be best practice to use multiple linked lists to hold the data.

Although both could get the job done a hash table is beest since it is the most efficient at key-value mapping.
Graphs and linked lists require pointer-based traversal to aqquire data. The hash table wins in efficiency and simplifing complex data relationships
```

### Sources:

