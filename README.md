# 2DPlatformerBugs

Pygame Platformer – Player Jitter Issue

Course: Pygame Course by DaFluffyPotato (YouTube)
Progress: 1.5 hours of 6-hour course completed


Issue Description
When implementing the platformer, the player sprite jitters when colliding vertically with "grass" tiles.

Observations:
The player moves smoothly until it collides with a platform.
On vertical collision, the player’s Rect is reset to the tile’s top every frame, causing small rapid movements (jittering).
Instead of stopping naturally on the top of the platform, the position keeps adjusting each frame.



Notes:
Issue only occurs on vertical collisions (falling onto tiles).
Horizontal collisions are working correctly.


when the player meets end of the tile rect 
it reset position to tile's rect top
instead of keep reseting position when it meets the top

<img width="232" height="213" alt="image" src="https://github.com/user-attachments/assets/1bbedc1f-30fc-482e-a5d2-56fcfec9f373" />


<img width="192" height="152" alt="image" src="https://github.com/user-attachments/assets/06c50ed0-ba61-44f7-8913-118c300e097a" />
