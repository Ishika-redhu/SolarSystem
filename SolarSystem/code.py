import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
             (100,80),
             2,
             (0,0,255)
             )

cv2.putText(img,
            "Mercury",
             (110,180),
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Venus",
             (190,270),
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Earth",
             (300,270),
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Mars",
             (400,250),0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Jupiter",
             (200,90),
             0.5,
             (255,255,255)
             )            
            
cv2.putText(img,
            "Saturn",
             (720,110),
            0.5,
             (255,255,255)
             ) 

cv2.putText(img,
            "Uranus",
             (970,120),
             0.5,
             (255,255,255)
             )
             
cv2.putText(img,
            "Neptune",
             (1020,120),
             0.5,
             (255,255,255)
             )


cv2.imshow("Output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_system_label.jpg",img)