### 18. Students Do: A Cartographer's Expedition (20 mins)

Students create map plots to visualize/embark on a virtual expedition through NYC to various places of interest.

Indicate to students that they should work in teams of 2-3 to plan the trip together.

**Instructions:**

* [README.md](Activities/18-Stu_Cartographers_Expedition/README.md)

**Files:**

* [cartographers_expedition.ipynb](Activities/18-Stu_Cartographers_Expedition/Unsolved/cartographers_expedition.ipynb)

### 19. Instructor Do: A Cartographers Expedition Activity Review (5 mins)

In this activity, student groups will present their maps and expeditions to the rest of the class.

**Files:**

* [cartographers_expedition.ipynb](Activities/18-Stu_Cartographers_Expedition/Solved/cartographers_expedition.ipynb)

Start the activity review by asking if there is a group who wants to volunteer to present their expedition first. Then, ask the following questions. If time remains, ask for a second group to also present.

* Ask the group to present their maps and to relay their full expedition.

  * **Answer** Airport -> Aqueduct Race Track -> Astoria Park -> Fort Totten -> Juniper Valley Park -> Madison Square

* Sometimes it's difficult to get a good understanding of whether or not two locations are close to one another. Were there any instances where you had to re-choose locations due to them being too far away?

  * **Answer** Yes. When picking locations at random, it was hard to determine which points would be close to one another.

* What are some programmatic approaches to making sure locations are close to one another?

  * **Answer** The data could be sorted by latitude and longitude.

  * **Answer** Data could have been sliced by borough first, and then places chosen from there.

* What guided your final decision on locations?

  * **Answer** Locations were chosen based off of categorical type and proximity. Locations of type garden, park, and square were chosen for a specific experience.

* Were the geographic scatter plots helpful in understanding the distribution of places of interest throughout NYC? How did the visual help cement the image?

  * **Answer** Yes, the plots were helpful. By color coding by **PlaceType**, it was easy to see the clusters of each type of place. This helped outline the trek through the boroughs. It was also helpful in noticing trends in positioning of certain locations (i.e. Ellis and Liberty Island are in same place and the forts all seem to be north of Manhattan.

Ask for any remaining questions before moving on.
