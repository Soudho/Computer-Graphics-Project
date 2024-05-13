# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random
#
# # truck = [350, 0]  #[350, 0, 350, 200]
# truck = {'x': 400, 'y': 400, 'direction': 'up'}
# # houseOriginalColors = [[[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], [[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], [[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], [[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], [[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]]]
# # houseColors = [[[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], [[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], [[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], [[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], [[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]]]
#
# house_li = [
#     {'x': 0, 'y': 0, 'health': 100, 'cond': 'normal',
#      'color': [[218 / 255, 165 / 255, 32 / 255], [184 / 255, 134 / 255, 30 / 255]],
#      'originalColor': [[218 / 255, 165 / 255, 32 / 255], [184 / 255, 134 / 255, 30 / 255]]},
#     {'x': 0, 'y': 250, 'health': 100, 'cond': 'normal',
#      'color': [[255 / 255, 0 / 255, 128 / 255], [128 / 255, 0 / 255, 64 / 255]],
#      'originalColor': [[255 / 255, 0 / 255, 128 / 255], [128 / 255, 0 / 255, 64 / 255]]},
#     {'x': 0, 'y': 500, 'health': 100, 'cond': 'normal',
#      'color': [[191 / 255, 0 / 255, 255 / 255], [115 / 255, 0 / 255, 153 / 255]],
#      'originalColor': [[191 / 255, 0 / 255, 255 / 255], [115 / 255, 0 / 255, 153 / 255]]},
#     {'x': 650, 'y': 0, 'health': 100, 'cond': 'normal',
#      'color': [[51 / 255, 102 / 255, 255 / 255], [0 / 255, 45 / 255, 179 / 255]],
#      'originalColor': [[51 / 255, 102 / 255, 255 / 255], [0 / 255, 45 / 255, 179 / 255]]},
#     {'x': 650, 'y': 250, 'health': 100, 'cond': 'normal',
#      'color': [[138 / 255, 138 / 255, 92 / 255], [92 / 255, 92 / 255, 61 / 255]],
#      'originalColor': [[138 / 255, 138 / 255, 92 / 255], [92 / 255, 92 / 255, 61 / 255]]},
#     {'x': 650, 'y': 500, 'health': 100, 'cond': 'normal',
#      'color': [[117 / 255, 117 / 255, 163 / 255], [71 / 255, 71 / 255, 107 / 255]],
#      'originalColor': [[117 / 255, 117 / 255, 163 / 255], [71 / 255, 71 / 255, 107 / 255]]}
# ]
#
# houseHealth = [[25, 160, 25 + house_li[0]['health'], 160], [25, 410, 25 + house_li[1]['health'], 410],
#                [25, 660, 25 + house_li[2]['health'], 660], [670, 160, 670 + house_li[3]['health'], 160],
#                [670, 410, 670 + house_li[4]['health'], 410], [670, 660, 670 + house_li[5]['health'], 660]]
# # house_li[0]['cond']='fire'
# fireTimer = 100
# water = -1
# score = 0
# fast_travel_left = 3
# gameover = -1
# restart = -1
# speed = 0
# pause = -1
#
#
# #################### Mid point line and circle algorithm:
# def drawPoint(x, y):
#     glBegin(GL_POINTS)
#     glVertex2i(x, y)
#     glEnd()
#
#
# def findZone(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     if abs(dx) >= abs(dy):
#         if dx >= 0 and dy >= 0:
#             return 0
#         elif dx <= 0 and dy >= 0:
#             return 3
#         elif dx <= 0 and dy <= 0:
#             return 4
#         elif dx >= 0 and dy <= 0:
#             return 7
#     else:
#         if dx >= 0 and dy >= 0:
#             return 1
#         elif dx <= 0 and dy >= 0:
#             return 2
#         elif dx <= 0 and dy <= 0:
#             return 5
#         elif dx >= 0 and dy <= 0:
#             return 6
#
#
# def convertToZone0(x, y, zone):
#     if zone == 0:
#         return x, y
#     elif zone == 1:
#         return y, x
#     elif zone == 2:
#         return y, -x
#     elif zone == 3:
#         return -x, y
#     elif zone == 4:
#         return -x, -y
#     elif zone == 5:
#         return -y, -x
#     elif zone == 6:
#         return -y, x
#     elif zone == 7:
#         return x, -y
#
#
# def convertToOriginalZone(x, y, zone):
#     if zone == 0:
#         return x, y
#     elif zone == 1:
#         return y, x
#     elif zone == 2:
#         return -y, x
#     elif zone == 3:
#         return -x, y
#     elif zone == 4:
#         return -x, -y
#     elif zone == 5:
#         return -y, -x
#     elif zone == 6:
#         return y, -x
#     elif zone == 7:
#         return x, -y
#
#
# def MidPointLineAlgorithm(x1, y1, x2, y2):
#     zone = findZone(x1, y1, x2, y2)
#
#     x1, y1 = convertToZone0(x1, y1, zone)
#     x2, y2 = convertToZone0(x2, y2, zone)
#
#     dx = x2 - x1
#     dy = y2 - y1
#     d = 2 * dy - dx
#     dE = 2 * dy
#     dNE = 2 * (dy - dx)
#     x = x1
#     y = y1
#     while (x <= x2):
#         x_original, y_original = convertToOriginalZone(x, y, zone)
#         drawPoint(x_original, y_original)
#         x += 1
#         if d > 0:
#             d += dNE
#             y = y + 1
#         else:
#             d += dE
#
#
# def drawPoints(x, y, dx, dy):
#     # global circles
#     # print(circles)
#     # if ((-375 <= x+dx <= 375) and (-375 <= -x+dx <= 375) and (-375 <= y+dx <= 375) and (-375 <= -y+dx <= 375) and (-375 <= y+dy <= 375) and (-375 <= -y+dy <= 375) and (-375 <= -x+dy <= 375) and (-375 <= x+dy <= 375)):
#     drawPoint(x + dx, y + dy)
#     drawPoint(-x + dx, y + dy)
#     drawPoint(-x + dx, -y + dy)
#     drawPoint(x + dx, -y + dy)
#     drawPoint(y + dx, x + dy)
#     drawPoint(-y + dx, x + dy)
#     drawPoint(-y + dx, -x + dy)
#     drawPoint(y + dx, -x + dy)
#
#
# def MidPointCircleAlgorithm(x, y, r):
#     x0 = 0
#     y0 = r
#     d = 1 - r
#     drawPoints(x0, y0, x, y)
#     while (x0 < y0):
#         if (d < 0):
#             d += (2 * x0 + 3)
#             x0 += 1
#         else:
#             d += ((2 * x0) - (2 * y0) + 5)
#             x0 += 1
#             y0 -= 1
#         drawPoints(x0, y0, x, y)
#
#
# ###########################################################################
# def buildHouse(x1, y1, color1, color2):
#     glPointSize(3)
#     glColor3f(*color1)
#     MidPointLineAlgorithm(x1 + 25, y1 + 20, x1 + 25, y1 + 135)
#     MidPointLineAlgorithm(x1 + 25, y1 + 135, x1 + 135, y1 + 135)
#     MidPointLineAlgorithm(x1 + 135, y1 + 135, x1 + 135, y1 + 20)
#     glPointSize(10)
#     MidPointLineAlgorithm(x1 + 30, y1 + 130, x1 + 130, y1 + 130)
#     MidPointLineAlgorithm(x1 + 30, y1 + 120, x1 + 130, y1 + 120)
#     MidPointLineAlgorithm(x1 + 30, y1 + 110, x1 + 30, y1 + 30)
#     MidPointLineAlgorithm(x1 + 60, y1 + 110, x1 + 60, y1 + 30)
#     MidPointLineAlgorithm(x1 + 70, y1 + 110, x1 + 70, y1 + 30)
#     MidPointLineAlgorithm(x1 + 80, y1 + 110, x1 + 80, y1 + 30)
#     MidPointLineAlgorithm(x1 + 90, y1 + 110, x1 + 90, y1 + 30)
#     MidPointLineAlgorithm(x1 + 100, y1 + 110, x1 + 100, y1 + 30)
#     MidPointLineAlgorithm(x1 + 130, y1 + 110, x1 + 130, y1 + 30)
#     MidPointLineAlgorithm(x1 + 30, y1 + 90, x1 + 130, y1 + 90)
#     MidPointLineAlgorithm(x1 + 30, y1 + 80, x1 + 130, y1 + 80)
#     MidPointLineAlgorithm(x1 + 30, y1 + 50, x1 + 130, y1 + 50)
#     MidPointLineAlgorithm(x1 + 30, y1 + 20, x1 + 130, y1 + 20)
#     glPointSize(3)
#     glColor3f(*color2)
#     MidPointLineAlgorithm(x1 + 25, y1 + 135, x1 + 17, y1 + 120)
#     MidPointLineAlgorithm(x1 + 17, y1 + 120, x1 + 17, y1 + 25)
#     glPointSize(8)
#     MidPointLineAlgorithm(x1 + 19, y1 + 120, x1 + 19, y1 + 25)
#     glPointSize(5)
#     MidPointLineAlgorithm(x1 + 25, y1 + 130, x1 + 25, y1 + 20)
#
#
# def buildHouses():
#     global houseHealth, pause, gameover
#     # global houseColors
#     global house_li
#     # House Serial: Bottom Left to Top Left, then, Bottom Right to Top Right
#     # buildHouse(0, 0,  houseColors[0][0], houseColors[0][1])
#     # buildHouse(0, 250,  houseColors[1][0], houseColors[1][1])
#     # buildHouse(0, 500,  houseColors[2][0], houseColors[2][1])
#     # buildHouse(650, 0,  houseColors[3][0], houseColors[3][1])
#     # buildHouse(650, 250,  houseColors[4][0], houseColors[4][1])
#     # buildHouse(650, 500,  houseColors[5][0], houseColors[5][1])
#
#     # buildHouse(house_li[0]['x'], house_li[0]['y'],  houseColors[0][0], houseColors[0][1])
#     # buildHouse(house_li[1]['x'], house_li[1]['y'],  houseColors[1][0], houseColors[1][1])
#     # buildHouse(house_li[2]['x'], house_li[2]['y'],  houseColors[2][0], houseColors[2][1])
#     # buildHouse(house_li[3]['x'], house_li[3]['y'],  houseColors[3][0], houseColors[3][1])
#     # buildHouse(house_li[4]['x'], house_li[4]['y'],  houseColors[4][0], houseColors[4][1])
#     # buildHouse(house_li[5]['x'], house_li[5]['y'],  houseColors[5][0], houseColors[5][1])
#
#     for house in house_li:
#         if (gameover == -1 and pause == -1):
#             if (house['cond'] == 'fire'):
#                 house['color'] = [[1, 0, 0], [0.4, 0, 0]]
#                 house['health'] -= 1  # 1  #0.001
#                 # print(house['health'])
#
#             if (house['cond'] == 'fire' and house['health'] <= 5):
#                 house['cond'] = 'burnt'
#                 house['health'] = 0
#
#             if (house['cond'] == 'burnt'):
#                 house['color'] = [[0.7, 0.7, 0.7], [0.7, 0.7, 0.7]]
#
#         buildHouse(house['x'], house['y'], house['color'][0], house['color'][1])
#
#
# def showHouseHealth():
#     global houseHealth
#     for i in range(len(houseHealth)):
#         glPointSize(15)
#         glColor3f(1, 0, 0)
#         MidPointLineAlgorithm(houseHealth[i][0], houseHealth[i][1], houseHealth[i][2], houseHealth[i][3])
#
#
# angle = 0
#
#
# def showTruck():
#     global angle, truck
#     tx = -40
#     ty = -75
#     glTranslatef(truck['x'], truck['y'], 0.0)  # change position from 0,0
#     glRotatef(angle, 0, 0, 1)  # change angle of object
#
#     glPointSize(5)
#     glColor3f(0, 0, 0)
#     MidPointCircleAlgorithm(tx, ty + 30, 5)
#     MidPointCircleAlgorithm(tx, ty + 15, 5)
#     MidPointCircleAlgorithm(tx, ty + 80, 5)
#     MidPointCircleAlgorithm(tx, ty + 95, 5)
#     MidPointCircleAlgorithm(tx + 80, ty + 30, 5)
#     MidPointCircleAlgorithm(tx + 80, ty + 15, 5)
#     MidPointCircleAlgorithm(tx + 80, ty + 80, 5)
#     MidPointCircleAlgorithm(tx + 80, ty + 95, 5)
#     glPointSize(4)
#     glColor3f(0, 0, 0)
#     MidPointLineAlgorithm(tx, ty, tx, ty + 120)
#     MidPointLineAlgorithm(tx, ty + 120, tx + 80, ty + 120)
#     MidPointLineAlgorithm(tx + 80, ty + 120, tx + 80, ty)
#     MidPointLineAlgorithm(tx, ty, tx + 80, ty)
#
#     if (gameover == -1):
#         glColor3f(179 / 255, 0, 0)
#     else:
#         glColor3f(0.2, 0.2, 0.2)
#     glPointSize(20)
#     MidPointLineAlgorithm(tx + 10, ty + 130, tx + 10, ty + 140)
#     MidPointLineAlgorithm(tx + 30, ty + 130, tx + 30, ty + 140)
#     MidPointLineAlgorithm(tx + 50, ty + 130, tx + 50, ty + 140)
#     MidPointLineAlgorithm(tx + 70, ty + 130, tx + 70, ty + 140)
#     glPointSize(5)
#     glColor3f(0, 0, 0)
#     MidPointLineAlgorithm(tx, ty + 120, tx + 80, ty + 120)
#     MidPointLineAlgorithm(tx, ty + 150, tx + 80, ty + 150)
#     MidPointLineAlgorithm(tx, ty + 120, tx, ty + 150)
#     MidPointLineAlgorithm(tx + 80, ty + 150, tx + 80, ty + 120)
#     glColor3f(204 / 255, 204 / 255, 204 / 255)
#     MidPointCircleAlgorithm(tx + 10, ty + 140, 3)
#     MidPointCircleAlgorithm(tx + 70, ty + 140, 3)
#
#     glPointSize(20)
#     if (gameover == -1):
#         glColor3f(200 / 255, 0, 0)
#     else:
#         glColor3f(0.2, 0.2, 0.2)
#     MidPointLineAlgorithm(tx + 10, ty + 5, tx + 10, ty + 105)
#     # glColor3f(200/255, 0, 0) #
#     MidPointLineAlgorithm(tx + 20, ty + 5, tx + 20, ty + 105)
#     # glColor3f(200/255, 0, 0)
#     MidPointLineAlgorithm(tx + 30, ty + 5, tx + 30, ty + 105)
#     # glColor3f(200/255, 0, 0) #
#     MidPointLineAlgorithm(tx + 40, ty + 5, tx + 40, ty + 105)
#     # glColor3f(200/255, 0, 0)
#     MidPointLineAlgorithm(tx + 50, ty + 5, tx + 50, ty + 105)
#     # glColor3f(200/255, 0, 0) #
#     MidPointLineAlgorithm(tx + 60, ty + 5, tx + 60, ty + 105)
#     # glColor3f(200/255, 0, 0)
#     MidPointLineAlgorithm(tx + 70, ty + 5, tx + 70, ty + 105)
#     # glColor3f(200/255, 0, 0) #
#     MidPointLineAlgorithm(tx + 60, ty + 5, tx + 60, ty + 105)
#     glPointSize(5)
#     if (gameover == -1):
#         glColor3f(200 / 255, 51 / 255, 51 / 255)
#     else:
#         glColor3f(0.2, 0.2, 0.2)
#     MidPointCircleAlgorithm(tx + 40, ty + 135, 3)
#     glColor3f(0, 0, 0)
#
#     MidPointLineAlgorithm(tx + 10, ty + 105, tx + 10, ty + 10)
#     MidPointLineAlgorithm(tx + 20, ty + 105, tx + 20, ty + 10)
#     MidPointLineAlgorithm(tx + 30, ty + 105, tx + 30, ty + 10)
#     MidPointLineAlgorithm(tx + 40, ty + 105, tx + 40, ty + 10)
#     MidPointLineAlgorithm(tx + 50, ty + 105, tx + 50, ty + 10)
#     MidPointLineAlgorithm(tx + 60, ty + 105, tx + 60, ty + 10)
#     MidPointLineAlgorithm(tx + 70, ty + 105, tx + 70, ty + 10)
#
#
# def showWater():
#     MidPointCircleAlgorithm(0, 110, 20)
#     MidPointCircleAlgorithm(-20, 140, 10)
#     MidPointCircleAlgorithm(20, 150, 15)
#     MidPointCircleAlgorithm(-5, 165, 13)
#
#
# def show_cross():
#     MidPointLineAlgorithm(745, 745, 775, 775)
#     MidPointLineAlgorithm(775, 745, 745, 775)
#
#
# def show_restart():
#     # glColor3f(0.5, 1.0, 1.0)
#     MidPointLineAlgorithm(20, 760, 50, 760)
#     MidPointLineAlgorithm(20, 760, 35, 770)
#     MidPointLineAlgorithm(20, 760, 35, 750)
#
#
# def show_pause():
#     MidPointLineAlgorithm(395, 745, 395, 775)
#     MidPointLineAlgorithm(405, 745, 405, 775)
#
#
# def show_play():
#     MidPointLineAlgorithm(395, 745, 395, 775)
#     MidPointLineAlgorithm(395, 745, 415, 760)
#     MidPointLineAlgorithm(395, 775, 415, 760)
#
#
# #########################################################################################
#
# def specialKeyListener(key, x, y):
#     global angle, truck, water, pause, gameover
#
#     if (gameover == -1 and pause == -1):
#         if key == GLUT_KEY_RIGHT:
#             angle = -90
#             if (truck['x'] + 30 <= 580):
#                 truck['x'] += 30
#             truck['direction'] = 'right'
#             water = -1
#         if key == GLUT_KEY_LEFT:
#             angle = 90
#             if (truck['x'] - 30 >= 220):
#                 truck['x'] -= 30
#             truck['direction'] = 'left'
#             water = -1
#         if key == GLUT_KEY_UP:
#             angle = 0
#             if (truck['y'] + 30 <= 650):
#                 truck['y'] += 30
#             truck['direction'] = 'up'
#             water = -1
#         if key == GLUT_KEY_DOWN:
#             angle = 180
#             truck['y'] -= 30
#             truck['direction'] = 'down'
#             water = -1
#
#     # print(truck['direction'])
#     # print(truck['x'], truck['y'])
#     glutPostRedisplay()
#
#
# def keyboardListener(key, x, y):
#     global water, gameover, pause
#     if (gameover == -1 and pause == -1):
#         if key == b' ':
#             water = -water
#     glutPostRedisplay()
#
#
# def mouseListener(button, state, x, y):
#     global truck, fast_travel_left, score, restart, pause, gameover
#     if button == GLUT_LEFT_BUTTON:
#         if (state == GLUT_DOWN):
#             # print(x,y)
#             if (x >= 220 and x <= 580 and y >= 150 and fast_travel_left > 0 and gameover == -1 and pause == -1):
#                 truck['x'] = x
#                 truck['y'] = 800 - y  # convert mouse coordinate
#                 fast_travel_left -= 1
#             print("Fast Travel Left:", fast_travel_left)
#
#             # print(x, y)
#             if (x > 730 and y < 60):
#                 print("Goodbye! Score:", score)
#                 glutLeaveMainLoop()
#
#             if (x <= 60 and y <= 60):
#                 # print('in')
#                 restart = 1
#
#             if (x > 378 and y < 65 and x < 420):
#                 # print('in')
#                 pause = -pause
#
#     glutPostRedisplay()
#
#
# def animate():
#     glutPostRedisplay()
#     global fireTimer, houseHealth, water, score, fast_travel_left, gameover, truck, house_li, restart, printGameOver, speed, pause
#     speed += 0.005
#
#     if (gameover == -1 and pause == -1):
#
#         if (fireTimer <= 0):
#             random_integer = random.randint(0, 5)
#             # print(random_integer)
#             house_li[random_integer]['cond'] = 'fire'
#             fireTimer = 100
#         fireTimer -= (3 + speed)  # 0.0075
#
#         houseHealth = [[25, 160, 25 + house_li[0]['health'], 160], [25, 410, 25 + house_li[1]['health'], 410],
#                        [25, 660, 25 + house_li[2]['health'], 660], [670, 160, 670 + house_li[3]['health'], 160],
#                        [670, 410, 670 + house_li[4]['health'], 410], [670, 660, 670 + house_li[5]['health'], 660]]
#
#         # checking if water is inside house on fire
#         if ((truck['y'] <= 130) and (truck['y'] >= 10) and (truck['direction'] == 'left')):
#             if ((truck['x'] <= 310) and water == 1 and house_li[0]['cond'] != 'burnt'):
#                 # print("in")
#                 if (house_li[0]['health'] <= 95):
#                     house_li[0]['health'] += 3  # 0.01
#                     if (house_li[0]['health'] >= 95):
#                         house_li[0]['cond'] = 'normal'
#                         score += 1
#                         print('Score:', score)
#                         house_li[0]['health'] = 100
#                         house_li[0]['color'] = house_li[0]['originalColor']
#
#         if ((truck['y'] <= 400) and (truck['y'] >= 280) and (truck['direction'] == 'left')):
#             if ((truck['x'] <= 310) and water == 1 and house_li[1]['cond'] != 'burnt'):
#                 # print("in")
#                 if (house_li[1]['health'] <= 95):
#                     house_li[1]['health'] += 3  # 0.01
#                     if (house_li[1]['health'] >= 95):
#                         house_li[1]['cond'] = 'normal'
#                         score += 1
#                         print('Score:', score)
#                         house_li[1]['health'] = 100
#                         house_li[1]['color'] = house_li[1]['originalColor']
#
#         if ((truck['y'] <= 640) and (truck['y'] >= 520) and (truck['direction'] == 'left')):
#             if ((truck['x'] <= 310) and water == 1 and house_li[2]['cond'] != 'burnt'):
#                 # print("in")
#                 if (house_li[2]['health'] <= 95):
#                     house_li[2]['health'] += 3  # 0.01
#                     if (house_li[2]['health'] >= 95):
#                         house_li[2]['cond'] = 'normal'
#                         score += 1
#                         print('Score:', score)
#                         house_li[2]['health'] = 100
#                         house_li[2]['color'] = house_li[2]['originalColor']
#
#         if ((truck['y'] <= 130) and (truck['y'] >= 10) and (truck['direction'] == 'right')):
#             if ((truck['x'] >= 490) and water == 1 and house_li[3]['cond'] != 'burnt'):
#                 # print("in")
#                 if (house_li[3]['health'] <= 95):
#                     house_li[3]['health'] += 3  # 0.01
#                     if (house_li[3]['health'] >= 95):
#                         house_li[3]['cond'] = 'normal'
#                         score += 1
#                         print('Score:', score)
#                         house_li[3]['health'] = 100
#                         house_li[3]['color'] = house_li[3]['originalColor']
#
#         if ((truck['y'] <= 370) and (truck['y'] >= 250) and (truck['direction'] == 'right')):
#             if ((truck['x'] >= 490) and water == 1 and house_li[4]['cond'] != 'burnt'):
#                 # print("in")
#                 if (house_li[4]['health'] <= 95):
#                     house_li[4]['health'] += 3  # 0.01
#                     if (house_li[4]['health'] >= 95):
#                         house_li[4]['cond'] = 'normal'
#                         score += 1
#                         print('Score:', score)
#                         house_li[4]['health'] = 100
#                         house_li[4]['color'] = house_li[4]['originalColor']
#         if ((truck['y'] <= 640) and (truck['y'] >= 490) and (truck['direction'] == 'right')):
#             if ((truck['x'] >= 490) and water == 1 and house_li[5]['cond'] != 'burnt'):
#                 # print("in")
#                 if (house_li[5]['health'] <= 95):
#                     house_li[5]['health'] += 3  # 0.01
#                     if (house_li[5]['health'] >= 95):
#                         house_li[5]['cond'] = 'normal'
#                         score += 1
#                         print('Score:', score)
#                         house_li[5]['health'] = 100
#                         house_li[5]['color'] = house_li[5]['originalColor']
#
#     if (restart == 1):
#         restart = -1
#         truck = {'x': 400, 'y': 400, 'direction': 'up'}
#         gameover = -1
#
#         house_li = [
#             {'x': 0, 'y': 0, 'health': 100, 'cond': 'normal',
#              'color': [[218 / 255, 165 / 255, 32 / 255], [184 / 255, 134 / 255, 30 / 255]],
#              'originalColor': [[218 / 255, 165 / 255, 32 / 255], [184 / 255, 134 / 255, 30 / 255]]},
#             {'x': 0, 'y': 250, 'health': 100, 'cond': 'normal',
#              'color': [[255 / 255, 0 / 255, 128 / 255], [128 / 255, 0 / 255, 64 / 255]],
#              'originalColor': [[255 / 255, 0 / 255, 128 / 255], [128 / 255, 0 / 255, 64 / 255]]},
#             {'x': 0, 'y': 500, 'health': 100, 'cond': 'normal',
#              'color': [[191 / 255, 0 / 255, 255 / 255], [115 / 255, 0 / 255, 153 / 255]],
#              'originalColor': [[191 / 255, 0 / 255, 255 / 255], [115 / 255, 0 / 255, 153 / 255]]},
#             {'x': 650, 'y': 0, 'health': 100, 'cond': 'normal',
#              'color': [[51 / 255, 102 / 255, 255 / 255], [0 / 255, 45 / 255, 179 / 255]],
#              'originalColor': [[51 / 255, 102 / 255, 255 / 255], [0 / 255, 45 / 255, 179 / 255]]},
#             {'x': 650, 'y': 250, 'health': 100, 'cond': 'normal',
#              'color': [[138 / 255, 138 / 255, 92 / 255], [92 / 255, 92 / 255, 61 / 255]],
#              'originalColor': [[138 / 255, 138 / 255, 92 / 255], [92 / 255, 92 / 255, 61 / 255]]},
#             {'x': 650, 'y': 500, 'health': 100, 'cond': 'normal',
#              'color': [[117 / 255, 117 / 255, 163 / 255], [71 / 255, 71 / 255, 107 / 255]],
#              'originalColor': [[117 / 255, 117 / 255, 163 / 255], [71 / 255, 71 / 255, 107 / 255]]}
#         ]
#
#         houseHealth = [[25, 160, 25 + house_li[0]['health'], 160], [25, 410, 25 + house_li[1]['health'], 410],
#                        [25, 660, 25 + house_li[2]['health'], 660], [670, 160, 670 + house_li[3]['health'], 160],
#                        [670, 410, 670 + house_li[4]['health'], 410], [670, 660, 670 + house_li[5]['health'], 660]]
#         # house_li[0]['cond']='fire'
#         # fireTimer = 100
#         water = -1
#         score = 0
#         fast_travel_left = 3
#         gameover = -1
#         printGameOver = 1
#         speed = 0
#
#
# # house_li[4]['cond']='fire'
# #####################################################################################
# def iterate():
#     glViewport(0, 0, 800, 800)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#
#
# printGameOver = 1
#
#
# def showScreen():
#     global water, gameover, score, printGameOver
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glClearColor(0 / 255, 60 / 255, 40 / 255, 1)  # (0, 128/255, 0, 1)
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     # glColor3f(1.0, 1.0, 0.0)
#     # call the draw methods here
#     # glColor3f(1, 1, 1)
#     # x1, y1 = 0, 0
#     # x2, y2 = 400, 400
#     # MidPointLineAlgorithm(x1, y1, x2, y2)
#     # MidPointCircleAlgorithm(400, 400, 50)
#     glPointSize(3)
#     glColor3f(179 / 255, 179 / 255, 179 / 255)
#     MidPointLineAlgorithm(400, 700, 400, 5)
#
#     glColor3f(1, 0, 0)
#     show_cross()
#     glColor3f(0.5, 1.0, 1.0)
#     show_restart()
#     if (pause == -1):
#         glColor3f(255 / 255, 140 / 255, 0)
#         show_pause()
#     elif (pause == 1):
#         glColor3f(255 / 255, 140 / 255, 0)
#         show_play()
#     showHouseHealth()
#     buildHouses()
#
#     showTruck()
#
#     num_burnt = 0
#     for house in house_li:
#         if (house['cond'] == 'burnt'):
#             num_burnt += 1
#         if (num_burnt >= 3):
#             gameover = 1
#             if (printGameOver == 1):
#                 print("Game Over!")
#                 print('Score:', score)
#             printGameOver = 0
#
#     if (water == 1):
#         glColor3f(0.0, 0.9, 0.9)
#         showWater()
#
#     glutSwapBuffers()
#
#
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(800, 800)  # window size
# glutInitWindowPosition(700, 25)
# wind = glutCreateWindow(b"CSE423 project")  # window name
# ################################
# glutDisplayFunc(showScreen)
# glutSpecialFunc(specialKeyListener)
# glutIdleFunc(animate)
# glutKeyboardFunc(keyboardListener)
# glutMouseFunc(mouseListener)
#
# glutMainLoop()
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

tank = {'x': 400, 'y': 400, 'direction': 'up'}
fireTimer = 100
Bullet = False
Score = 0
fast_travel_left = 3
gameover = False
restart = False
angle = 0
speed = 0
pause = False
printGameOver = True

house_area = [{'x': 10, 'y': 20, 'health': 100, 'condition': 'normal', 'color': [[0.9, 0.6, 0.1], [0.7, 0.5, 0.1]],
               'originalColor': [[0.9, 0.6, 0.1], [0.7, 0.5, 0.1]]},
              {'x': 10, 'y': 220, 'health': 100, 'condition': 'normal', 'color': [[1.0, 0.0, 0.5], [0.5, 0.0, 0.3]],
               'originalColor': [[1.0, 0.0, 0.5], [0.5, 0.0, 0.3]]},
              {'x': 10, 'y': 420, 'health': 100, 'condition': 'normal', 'color': [[0.9, 0.0, 1.0], [0.5, 0.0, 0.6]],
               'originalColor': [[0.9, 0.0, 1.0], [0.5, 0.0, 0.6]]},
              {'x': 640, 'y': 20, 'health': 100, 'condition': 'normal', 'color': [[0.1, 0.3, 1.0], [0.0, 0.2, 0.7]],
               'originalColor': [[0.1, 0.3, 1.0], [0.0, 0.2, 0.7]]},
              {'x': 640, 'y': 220, 'health': 100, 'condition': 'normal', 'color': [[0.2, 0.4, 0.2], [0.2, 0.2, 0.2]],
               'originalColor': [[0.2, 0.4, 0.2], [0.2, 0.2, 0.2]]},
              {'x': 640, 'y': 420, 'health': 100, 'condition': 'normal', 'color': [[1, 0.5, 0.6], [0.3, 0.3, 0.4]],
               'originalColor': [[1, 0.5, 0.6], [0.3, 0.3, 0.4]]}]

HouseHealth = [[25, 180, 45 + house_area[0]['health'], 180], [25, 380, 45 + house_area[1]['health'], 380],
               [25, 580, 45 + house_area[2]['health'], 580], [655, 180, 675 + house_area[3]['health'], 180],
               [655, 380, 675 + house_area[4]['health'], 380], [655, 580, 675 + house_area[5]['health'], 580]]


# ------------------------ MIDPOINT LINE DRAWING ALGORITHM START ------------------------

def draw_Point(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


def Find_Zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 and dy <= 0:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 and dy <= 0:
            return 6


def Convert_To_Zone_0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def Convert_To_Original_Zone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def Mid_Point_Line_Algorithm(x1, y1, x2, y2):
    zone = Find_Zone(x1, y1, x2, y2)

    x1, y1 = Convert_To_Zone_0(x1, y1, zone)
    x2, y2 = Convert_To_Zone_0(x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x = x1
    y = y1
    while (x <= x2):
        x_original, y_original = Convert_To_Original_Zone(x, y, zone)
        draw_Point(x_original, y_original)
        x += 1
        if d > 0:
            d += dNE
            y = y + 1
        else:
            d += dE


# ------------------------ MIDPOINT LINE DRAWING ALGORITHM END ------------------------

# ------------------------ MIDPOINT CIRCLE DRAWING ALGORITHM START ------------------------


def draw_Points(x, y, dx, dy):
    draw_Point(x + dx, y + dy)
    draw_Point(-x + dx, y + dy)
    draw_Point(-x + dx, -y + dy)
    draw_Point(x + dx, -y + dy)
    draw_Point(y + dx, x + dy)
    draw_Point(-y + dx, x + dy)
    draw_Point(-y + dx, -x + dy)
    draw_Point(y + dx, -x + dy)


def Mid_Point_Circle_Algorithm(x, y, r):
    x0 = 0
    y0 = r
    d = 1 - r
    draw_Points(x0, y0, x, y)
    while (x0 < y0):
        if (d < 0):
            d += (2 * x0 + 3)
            x0 += 1
        else:
            d += ((2 * x0) - (2 * y0) + 5)
            x0 += 1
            y0 -= 1
        draw_Points(x0, y0, x, y)


# ------------------------ MIDPOINT CIRCLE DRAWING ALGORITHM END ------------------------

# ------------------------ DRAW HOUSES ------------------------

def Draw_Houses(x1, y1, color1, color2):
    glPointSize(25)
    glColor3f(0.2, 0.7, 0.8)
    Mid_Point_Line_Algorithm(x1 + 37, y1 + 90, x1 + 37, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 70, y1 + 90, x1 + 70, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 80, y1 + 90, x1 + 80, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 112, y1 + 90, x1 + 112, y1 + 20)

    glPointSize(2)
    glColor3f(0.2, 0.2, 0.2)
    Mid_Point_Line_Algorithm(x1 + 38, y1 + 90, x1 + 38, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 75, y1 + 90, x1 + 75, y1 + 50)
    Mid_Point_Line_Algorithm(x1 + 112, y1 + 90, x1 + 112, y1 + 20)

    Mid_Point_Line_Algorithm(x1 + 20, y1 + 73, x1 + 130, y1 + 73)
    Mid_Point_Line_Algorithm(x1 + 60, y1 + 38, x1 + 20, y1 + 38)
    Mid_Point_Line_Algorithm(x1 + 100, y1 + 38, x1 + 130, y1 + 38)

    Mid_Point_Line_Algorithm(x1 + 75, y1 + 50, x1 + 75, y1 + 10)
    Mid_Point_Circle_Algorithm(x1 + 70, y1 + 32, 1)
    Mid_Point_Circle_Algorithm(x1 + 80, y1 + 32, 1)

    glPointSize(12)
    if (gameover == False):
        glColor3f(*color1)
    else:
        glColor3f(1, 1, 1)

    Mid_Point_Line_Algorithm(x1 + 25, y1 + 90, x1 + 125, y1 + 90)
    Mid_Point_Line_Algorithm(x1 + 25, y1 + 55, x1 + 125, y1 + 55)
    Mid_Point_Line_Algorithm(x1 + 25, y1 + 20, x1 + 55, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 95, y1 + 20, x1 + 125, y1 + 20)

    Mid_Point_Line_Algorithm(x1 + 20, y1 + 90, x1 + 20, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 55, y1 + 90, x1 + 55, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 95, y1 + 90, x1 + 95, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 130, y1 + 90, x1 + 130, y1 + 20)

    glPointSize(8)
    glColor3f(0.2, 0.2, 0.2)
    Mid_Point_Line_Algorithm(x1 + 10, y1 + 10, x1 + 140, y1 + 10)
    Mid_Point_Line_Algorithm(x1 + 12, y1 + 100, x1 + 138, y1 + 100)

    glPointSize(4)
    glColor3f(0.5, 0.5, 0.5)
    Mid_Point_Line_Algorithm(x1 + 72, y1 + 128, x1 + 77, y1 + 128)
    Mid_Point_Line_Algorithm(x1 + 66, y1 + 124, x1 + 85, y1 + 124)
    Mid_Point_Line_Algorithm(x1 + 58, y1 + 120, x1 + 93, y1 + 120)
    Mid_Point_Line_Algorithm(x1 + 50, y1 + 116, x1 + 101, y1 + 116)
    Mid_Point_Line_Algorithm(x1 + 40, y1 + 112, x1 + 111, y1 + 112)
    Mid_Point_Line_Algorithm(x1 + 32, y1 + 108, x1 + 119, y1 + 108)
    Mid_Point_Line_Algorithm(x1 + 29, y1 + 105, x1 + 122, y1 + 105)

    glPointSize(2)
    glColor3f(1, 1, 0)
    Mid_Point_Line_Algorithm(x1 + 72, y1 + 120, x1 + 72, y1 + 110)
    Mid_Point_Circle_Algorithm(x1 + 75, y1 + 118, 3)
    Mid_Point_Circle_Algorithm(x1 + 75, y1 + 112, 3)

    glPointSize(3)
    glColor3f(0.2, 0.2, 0.2)
    Mid_Point_Line_Algorithm(x1 + 28, y1 + 104, x1 + 122, y1 + 104)
    Mid_Point_Line_Algorithm(x1 + 20, y1 + 102, x1 + 75, y1 + 130)
    Mid_Point_Line_Algorithm(x1 + 75, y1 + 130, x1 + 130, y1 + 102)

    glPointSize(2)
    glColor3f(0.5, 0.5, 0.5)

    Mid_Point_Line_Algorithm(x1 + 12, y1 + 15, x1 + 138, y1 + 15)
    Mid_Point_Line_Algorithm(x1 + 12, y1 + 95, x1 + 138, y1 + 95)
    Mid_Point_Line_Algorithm(x1 + 8, y1 + 102, x1 + 142, y1 + 102)
    Mid_Point_Line_Algorithm(x1 + 5, y1 + 8, x1 + 145, y1 + 8)

    glPointSize(8)
    glColor3f(0.5, 0.5, 0.5)
    Mid_Point_Line_Algorithm(x1 + 20, y1 + 90, x1 + 20, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 55, y1 + 90, x1 + 55, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 95, y1 + 90, x1 + 95, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 130, y1 + 90, x1 + 130, y1 + 20)

    glPointSize(2)
    glColor3f(0.2, 0.2, 0.2)
    Mid_Point_Line_Algorithm(x1 + 18, y1 + 90, x1 + 18, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 22, y1 + 90, x1 + 22, y1 + 20)

    Mid_Point_Line_Algorithm(x1 + 53, y1 + 90, x1 + 53, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 57, y1 + 90, x1 + 57, y1 + 20)

    Mid_Point_Line_Algorithm(x1 + 93, y1 + 90, x1 + 93, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 97, y1 + 90, x1 + 97, y1 + 20)

    Mid_Point_Line_Algorithm(x1 + 128, y1 + 90, x1 + 128, y1 + 20)
    Mid_Point_Line_Algorithm(x1 + 132, y1 + 90, x1 + 132, y1 + 20)


def Draw_House():
    global HouseHealth, pause, gameover, house_area

    for house in house_area:
        if (gameover == False and pause == False):
            if (house['condition'] == 'looting'):
                house['color'] = [[1, 0, 0], [0.4, 0, 0]]
                house['health'] -= 1

            if (house['condition'] == 'looting' and house['health'] <= 5):
                house['condition'] = 'looted'
                house['health'] = 0

            if (house['condition'] == 'looted'):
                house['color'] = [[0.7, 0.7, 0.7], [0.7, 0.7, 0.7]]
        Draw_Houses(house['x'], house['y'], house['color'][0], house['color'][1])


def Draw_HouseHealth():
    global HouseHealth
    for i in range(len(HouseHealth)):
        glPointSize(10)
        glColor3f(0.8, 0, 0)
        Mid_Point_Line_Algorithm(HouseHealth[i][0], HouseHealth[i][1], HouseHealth[i][2], HouseHealth[i][3])


# ------------------------ DRAW Roads ------------------------

def Draw_RoadLines():
    glPointSize(12)
    glColor3f(0.7, 0.5, 0)
    Mid_Point_Line_Algorithm(400, 560, 400, 510)
    Mid_Point_Line_Algorithm(400, 460, 400, 410)
    Mid_Point_Line_Algorithm(400, 360, 400, 310)
    Mid_Point_Line_Algorithm(400, 260, 400, 210)
    Mid_Point_Line_Algorithm(400, 160, 400, 110)
    Mid_Point_Line_Algorithm(400, 60, 400, 30)


# ------------------------ DRAW TANK ------------------------

def Draw_Tank():
    global angle, tank
    tx = -40
    ty = -75
    glTranslatef(tank['x'], tank['y'], 0.0)
    glRotatef(angle, 0, 0, 1)
    # draw wheel of the tank
    glPointSize(5)
    glColor3f(0, 0, 0)
    # left wheels
    Mid_Point_Circle_Algorithm(tx, ty + 15, 5)
    Mid_Point_Circle_Algorithm(tx, ty + 30, 5)
    Mid_Point_Circle_Algorithm(tx, ty + 45, 5)
    Mid_Point_Circle_Algorithm(tx, ty + 60, 5)
    Mid_Point_Circle_Algorithm(tx, ty + 75, 5)
    Mid_Point_Circle_Algorithm(tx, ty + 90, 5)
    # right wheels
    Mid_Point_Circle_Algorithm(tx + 79, ty + 15, 5)
    Mid_Point_Circle_Algorithm(tx + 79, ty + 30, 5)
    Mid_Point_Circle_Algorithm(tx + 79, ty + 45, 5)
    Mid_Point_Circle_Algorithm(tx + 79, ty + 60, 5)
    Mid_Point_Circle_Algorithm(tx + 79, ty + 75, 5)
    Mid_Point_Circle_Algorithm(tx + 79, ty + 90, 5)

    Mid_Point_Circle_Algorithm(tx + 40, ty + 155, 2)

    glPointSize(9)
    if (gameover == False):
        glColor3f(0.2, 0, 0)
    else:
        glColor3f(0, 0, 0)

    Mid_Point_Circle_Algorithm(tx + 15, ty - 3, 3)
    Mid_Point_Circle_Algorithm(tx + 65, ty - 3, 3)

    glPointSize(4)
    glColor3f(0, 0, 0)
    Mid_Point_Line_Algorithm(tx, ty, tx, ty + 110)
    Mid_Point_Line_Algorithm(tx + 20, ty + 115, tx + 60, ty + 115)
    Mid_Point_Line_Algorithm(tx, ty + 110, tx + 20, ty + 110)
    Mid_Point_Line_Algorithm(tx + 60, ty + 110, tx + 80, ty + 110)
    Mid_Point_Line_Algorithm(tx + 80, ty + 110, tx + 80, ty)
    Mid_Point_Line_Algorithm(tx, ty - 5, tx + 80, ty - 5)

    if (gameover == False):
        glColor3f(179 / 255, 0, 0)
    else:
        glColor3f(0.2, 0.2, 0.2)

    glPointSize(20)
    if (gameover == False):
        glColor3f(0.1, 0.1, 0)
    else:
        glColor3f(0.2, 0.2, 0.2)
    Mid_Point_Line_Algorithm(tx + 10, ty + 5, tx + 10, ty + 100)
    Mid_Point_Line_Algorithm(tx + 20, ty + 5, tx + 20, ty + 105)
    Mid_Point_Line_Algorithm(tx + 30, ty + 5, tx + 30, ty + 105)
    Mid_Point_Line_Algorithm(tx + 40, ty + 5, tx + 40, ty + 105)
    Mid_Point_Line_Algorithm(tx + 50, ty + 5, tx + 50, ty + 105)
    Mid_Point_Line_Algorithm(tx + 60, ty + 5, tx + 60, ty + 105)
    Mid_Point_Line_Algorithm(tx + 70, ty + 5, tx + 70, ty + 100)

    glPointSize(5)
    if (gameover == False):
        glColor3f(1, 1, 1)
    else:
        glColor3f(0, 0, 0)

    Mid_Point_Circle_Algorithm(tx + 14, ty + 118, 1)
    Mid_Point_Circle_Algorithm(tx + 66, ty + 118, 1)

    glPointSize(9)
    if (gameover == False):
        glColor3f(0.2, 0.2, 0)
    else:
        glColor3f(0, 0, 0)
    Mid_Point_Line_Algorithm(tx + 14, ty + 115, tx + 14, ty + 115)
    Mid_Point_Line_Algorithm(tx + 66, ty + 115, tx + 66, ty + 115)

    glPointSize(5)
    if (gameover == False):
        glColor3f(200 / 255, 51 / 255, 51 / 255)
    else:
        glColor3f(0.2, 0.2, 0.2)

    glPointSize(2)
    glColor3f(0, 0, 0)
    Mid_Point_Line_Algorithm(tx + 10, ty - 5, tx + 10, ty + 100)
    Mid_Point_Line_Algorithm(tx + 10, ty + 100, tx + 70, ty + 100)
    Mid_Point_Line_Algorithm(tx + 70, ty - 5, tx + 70, ty + 100)

    glPointSize(20)
    if (gameover == False):
        glColor3f(0.1, 0.2, 0)
    else:
        glColor3f(0.2, 0.2, 0.2)
    Mid_Point_Line_Algorithm(tx + 20, ty + 5, tx + 20, ty + 90)
    Mid_Point_Line_Algorithm(tx + 30, ty + 5, tx + 30, ty + 90)
    Mid_Point_Line_Algorithm(tx + 40, ty + 5, tx + 40, ty + 90)
    Mid_Point_Line_Algorithm(tx + 50, ty + 5, tx + 50, ty + 90)
    Mid_Point_Line_Algorithm(tx + 60, ty + 5, tx + 60, ty + 90)

    glPointSize(8)
    if (gameover == False):
        glColor3f(0, 0.1, 0)
    else:
        glColor3f(0, 0, 0)
    Mid_Point_Line_Algorithm(tx + 40, ty + 70, tx + 40, ty + 150)
    Mid_Point_Circle_Algorithm(tx + 40, ty + 80, 4)
    Mid_Point_Circle_Algorithm(tx + 40, ty + 150, 4)
    Mid_Point_Circle_Algorithm(tx + 40, ty + 70, 8)
    Mid_Point_Circle_Algorithm(tx + 40, ty + 40, 9)

    glPointSize(30)
    if (gameover == False):
        glColor3f(0, 0.1, 0)
    else:
        glColor3f(0, 0, 0)
    Mid_Point_Line_Algorithm(tx + 40, ty + 50, tx + 40, ty + 60)

    glPointSize(2)
    if (gameover == False):
        glColor3f(0.1, 0, 0)
    else:
        glColor3f(0, 0, 0)

    Mid_Point_Circle_Algorithm(tx + 20, ty + 90, 1)
    Mid_Point_Circle_Algorithm(tx + 60, ty + 90, 1)
    Mid_Point_Circle_Algorithm(tx + 40, ty + 55, 8)
    Mid_Point_Circle_Algorithm(tx + 40, ty + 55, 4)
    Mid_Point_Circle_Algorithm(tx + 40, ty + 35, 2)
    Mid_Point_Circle_Algorithm(tx + 20, ty + 10, 5)
    Mid_Point_Circle_Algorithm(tx + 20, ty + 10, 1)
    Mid_Point_Circle_Algorithm(tx + 30, ty, 1)
    Mid_Point_Circle_Algorithm(tx + 60, ty + 10, 5)
    Mid_Point_Circle_Algorithm(tx + 60, ty + 10, 1)
    Mid_Point_Circle_Algorithm(tx + 50, ty, 1)


# ------------------------ DRAW Bullets ------------------------

def Draw_Bullet():
    glPointSize(4)
    glColor3f(0, 0, 0)
    Mid_Point_Circle_Algorithm(0, 155, 4)
    Mid_Point_Circle_Algorithm(20, 140, 4)
    Mid_Point_Circle_Algorithm(-20, 140, 4)
    Mid_Point_Circle_Algorithm(0, 110, 4)
    Mid_Point_Circle_Algorithm(0, 155, 1)
    Mid_Point_Circle_Algorithm(20, 140, 1)
    Mid_Point_Circle_Algorithm(-20, 140, 1)
    Mid_Point_Circle_Algorithm(0, 110, 1)


# ------------------------ DRAW Buttons ------------------------

def Draw_Cross():
    glPointSize(4)
    glColor3f(1, 0.1, 0)
    Mid_Point_Line_Algorithm(740, 640, 780, 680)
    Mid_Point_Line_Algorithm(780, 640, 740, 680)


def Draw_Restart():
    glPointSize(4)
    glColor3f(0, 0.8, 0.5)
    Mid_Point_Line_Algorithm(20, 660, 70, 660)
    Mid_Point_Line_Algorithm(20, 660, 40, 680)
    Mid_Point_Line_Algorithm(20, 660, 40, 640)


def Draw_Pause():
    glColor3f(1, 1, 0)
    glPointSize(6)
    Mid_Point_Line_Algorithm(385, 640, 385, 680)
    Mid_Point_Line_Algorithm(415, 640, 415, 680)


def Draw_Play():
    glPointSize(4)
    glColor3f(0.2, 1, 0)
    Mid_Point_Line_Algorithm(385, 640, 385, 680)
    Mid_Point_Line_Algorithm(385, 640, 420, 660)
    Mid_Point_Line_Algorithm(385, 680, 420, 660)


# ------------------------ DISPLAY SCORE AND FAST TRAVEL ------------------------

def Render_Text(string, x, y, font):
    glRasterPos2f(x, y)
    for character in string:
        glutBitmapCharacter(font, ord(character))  # type: ignore


def Show_Score():
    global Score
    glColor3f(0.2, 1, 0)
    Score_text = f"Your Score: {Score}"
    Render_Text(Score_text, 150, 650, GLUT_BITMAP_TIMES_ROMAN_24)  # type: ignore


def Show_Fast_Travel_Left():
    global fast_travel_left
    glColor3f(0.2, 1, 0)
    life_text = f"Fast Travel Left: {fast_travel_left}"
    Render_Text(life_text, 500, 650, GLUT_BITMAP_TIMES_ROMAN_24)  # type: ignore


# ------------------------ KEYBOARD AND MOUSE COMMANDS ------------------------

def SpecialKeyListener(key, x, y):
    global angle, tank, Bullet, pause, gameover

    if (gameover == False and pause == False):
        if key == GLUT_KEY_RIGHT:
            angle = -90
            if (tank['x'] + 30 <= 570):
                tank['x'] += 30
            tank['direction'] = 'right'
            Bullet = False
        if key == GLUT_KEY_LEFT:
            angle = 90
            if (tank['x'] - 30 >= 230):
                tank['x'] -= 30
            tank['direction'] = 'left'
            Bullet = False
        if key == GLUT_KEY_UP:
            angle = 0
            if (tank['y'] + 30 <= 500):
                tank['y'] += 30
            tank['direction'] = 'up'
            Bullet = False
        if key == GLUT_KEY_DOWN:
            angle = 180
            if (tank['y'] - 30 >= 80):
                tank['y'] -= 30
            tank['direction'] = 'down'
            Bullet = False

    glutPostRedisplay()


def keyboardListener(key, x, y):
    global Bullet, gameover, pause
    if (gameover == False and pause == False):
        if key == b' ':
            Bullet = not Bullet

    glutPostRedisplay()


def MouseListener(button, state, x, y):
    global tank, fast_travel_left, Score, restart, pause, gameover
    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):
            if (x >= 230 and x <= 570 and y >= 220 and fast_travel_left > 0 and gameover == False and pause == False):
                tank['x'] = x
                tank['y'] = 720 - y
                fast_travel_left -= 1
            print("Fast Travel Left:", fast_travel_left)

            if (x >= 720 and y <= 70):
                print("Goodbye! Score:", Score)
                glutLeaveMainLoop()
            if (x <= 70 and y <= 70):
                restart = True
            if (x > 370 and y < 70 and x < 430):
                pause = not pause

    glutPostRedisplay()


# ------------------------ ANIMATIONS ------------------------

def Animation():
    glutPostRedisplay()
    global fireTimer, HouseHealth, Bullet, Score, fast_travel_left, gameover, tank, house_area, restart, printGameOver, speed, pause
    speed += 0.005

    if (gameover == False and pause == False):

        if (fireTimer <= 0):
            random_integer = random.randint(0, 5)
            house_area[random_integer]['condition'] = 'looting'
            fireTimer = 100

        fireTimer -= (3 + speed)

        HouseHealth = [[25, 180, 45 + house_area[0]['health'], 180], [25, 380, 45 + house_area[1]['health'], 380],
                       [25, 580, 45 + house_area[2]['health'], 580], [655, 180, 675 + house_area[3]['health'], 180],
                       [655, 380, 675 + house_area[4]['health'], 380], [655, 580, 675 + house_area[5]['health'], 580]]

        if ((tank['y'] <= 130) and (tank['y'] >= 50) and (tank['direction'] == 'left')):
            if ((tank['x'] <= 310) and Bullet == True and house_area[0]['condition'] != 'looted'):
                if (house_area[0]['health'] <= 95):
                    house_area[0]['health'] += 3
                    if (house_area[0]['health'] >= 95):
                        house_area[0]['condition'] = 'normal'
                        Score += 1
                        print('Score:', Score)
                        house_area[0]['health'] = 100
                        house_area[0]['color'] = house_area[0]['originalColor']

        if ((tank['y'] <= 330) and (tank['y'] >= 250) and (tank['direction'] == 'left')):
            if ((tank['x'] <= 310) and Bullet == True and house_area[1]['condition'] != 'looted'):
                if (house_area[1]['health'] <= 95):
                    house_area[1]['health'] += 3
                    if (house_area[1]['health'] >= 95):
                        house_area[1]['condition'] = 'normal'
                        Score += 1
                        print('Score:', Score)
                        house_area[1]['health'] = 100
                        house_area[1]['color'] = house_area[1]['originalColor']

        if ((tank['y'] <= 530) and (tank['y'] >= 450) and (tank['direction'] == 'left')):
            if ((tank['x'] <= 310) and Bullet == True and house_area[2]['condition'] != 'looted'):
                if (house_area[2]['health'] <= 95):
                    house_area[2]['health'] += 3
                    if (house_area[2]['health'] >= 95):
                        house_area[2]['condition'] = 'normal'
                        Score += 1
                        print('Score:', Score)
                        house_area[2]['health'] = 100
                        house_area[2]['color'] = house_area[2]['originalColor']

        if ((tank['y'] <= 130) and (tank['y'] >= 50) and (tank['direction'] == 'right')):
            if ((tank['x'] >= 490) and Bullet == True and house_area[3]['condition'] != 'looted'):
                if (house_area[3]['health'] <= 95):
                    house_area[3]['health'] += 3
                    if (house_area[3]['health'] >= 95):
                        house_area[3]['condition'] = 'normal'
                        Score += 1
                        print('Score:', Score)
                        house_area[3]['health'] = 100
                        house_area[3]['color'] = house_area[3]['originalColor']

        if ((tank['y'] <= 330) and (tank['y'] >= 250) and (tank['direction'] == 'right')):
            if ((tank['x'] >= 490) and Bullet == True and house_area[4]['condition'] != 'looted'):
                if (house_area[4]['health'] <= 95):
                    house_area[4]['health'] += 3
                    if (house_area[4]['health'] >= 95):
                        house_area[4]['condition'] = 'normal'
                        Score += 1
                        print('Score:', Score)
                        house_area[4]['health'] = 100
                        house_area[4]['color'] = house_area[4]['originalColor']

        if ((tank['y'] <= 530) and (tank['y'] >= 450) and (tank['direction'] == 'right')):
            if ((tank['x'] >= 490) and Bullet == True and house_area[5]['condition'] != 'looted'):
                if (house_area[5]['health'] <= 95):
                    house_area[5]['health'] += 3
                    if (house_area[5]['health'] >= 95):
                        house_area[5]['condition'] = 'normal'
                        Score += 1
                        print('Score:', Score)
                        house_area[5]['health'] = 100
                        house_area[5]['color'] = house_area[5]['originalColor']

    if (restart == True):
        restart = False
        tank = {'x': 400, 'y': 400, 'direction': 'up'}
        gameover = False

        house_area = [
            {'x': 10, 'y': 20, 'health': 100, 'condition': 'normal', 'color': [[0.9, 0.6, 0.1], [0.7, 0.5, 0.1]],
             'originalColor': [[0.9, 0.6, 0.1], [0.7, 0.5, 0.1]]},
            {'x': 10, 'y': 220, 'health': 100, 'condition': 'normal', 'color': [[1.0, 0.0, 0.5], [0.5, 0.0, 0.3]],
             'originalColor': [[1.0, 0.0, 0.5], [0.5, 0.0, 0.3]]},
            {'x': 10, 'y': 420, 'health': 100, 'condition': 'normal', 'color': [[0.9, 0.0, 1.0], [0.5, 0.0, 0.6]],
             'originalColor': [[0.9, 0.0, 1.0], [0.5, 0.0, 0.6]]},
            {'x': 640, 'y': 20, 'health': 100, 'condition': 'normal', 'color': [[0.1, 0.3, 1.0], [0.0, 0.2, 0.7]],
             'originalColor': [[0.1, 0.3, 1.0], [0.0, 0.2, 0.7]]},
            {'x': 640, 'y': 220, 'health': 100, 'condition': 'normal', 'color': [[0.2, 0.4, 0.2], [0.2, 0.2, 0.2]],
             'originalColor': [[0.2, 0.4, 0.2], [0.2, 0.2, 0.2]]},
            {'x': 640, 'y': 420, 'health': 100, 'condition': 'normal', 'color': [[1, 0.5, 0.6], [0.3, 0.3, 0.4]],
             'originalColor': [[1, 0.5, 0.6], [0.3, 0.3, 0.4]]}]

        HouseHealth = [[25, 180, 45 + house_area[0]['health'], 180], [25, 380, 45 + house_area[1]['health'], 380],
                       [25, 580, 45 + house_area[2]['health'], 580], [655, 180, 675 + house_area[3]['health'], 180],
                       [655, 380, 675 + house_area[4]['health'], 380], [655, 580, 675 + house_area[5]['health'], 580]]

        Bullet = False
        Score = 0
        fast_travel_left = 3
        printGameOver = True
        pause = False
        speed = 0


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def Display():
    global Bullet, gameover, Score, printGameOver
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.1, 0.1, 0.1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    Draw_RoadLines()
    glColor3f(1, 0, 0)
    Draw_Cross()
    glColor3f(0.5, 1.0, 1.0)
    Draw_Restart()

    if (gameover == False and pause == False):
        Draw_Pause()
    elif (gameover == False and pause == True):
        Draw_Play()

    if (gameover == False):
        Show_Score()
        Show_Fast_Travel_Left()

    if (gameover == True):
        glColor3f(1, 0, 0)
        Render_Text("Game Over..!", 335, 650, GLUT_BITMAP_TIMES_ROMAN_24)  # type: ignore
        glColor3f(0.2, 1, 0)
        Score_text = f"Your Score: {Score}"
        Render_Text(Score_text, 335, 610, GLUT_BITMAP_TIMES_ROMAN_24)  # type: ignore

    Draw_HouseHealth()
    Draw_House()
    Draw_Tank()

    num_looted = 0
    for house in house_area:
        if (house['condition'] == 'looted'):
            num_looted += 1
        if (num_looted >= 3):
            gameover = True
            if (printGameOver == True):
                print("Game Over!")
                print('Score:', Score)
            printGameOver = False

    if (Bullet == True):
        glColor3f(0.0, 0.9, 0.9)
        Draw_Bullet()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 700)
glutInitWindowPosition(400, 25)
wind = glutCreateWindow(b"Money Heist Game!")
glutIdleFunc(Animation)
glutDisplayFunc(Display)
glutSpecialFunc(SpecialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(MouseListener)
glutMainLoop()