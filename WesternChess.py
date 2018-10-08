#Chess
import turtle
import random


#Go to the middle of the square
def goToSqr(sqrNo, tgTurtle, noAnim):
    x = (sqrNo%8) * widthSqrSize - boardWidth/2 + widthSqrSize / 2;
    y = int(sqrNo/8) * heightSqrSize - boardHeight/2 + heightSqrSize;
    posX = tgTurtle.xcor();
    posY = tgTurtle.ycor();
    if (abs((0.001 + posX - x) / (0.001 + x)) > 0.011 or abs((0.001 + posY - y) / (0.001 + y)) > 0.011):
        if (noAnim == 1):
            turtle.tracer(0,0);
        else:
            turtle.tracer(1,50);
        tgTurtle.goto(x, y);
        turtle.tracer(0,0);
  
def drawSqr():
    turtle0.down();
    turtle0.begin_fill();
    posX = turtle0.xcor();
    posY = turtle0.ycor();
    turtle0.goto(posX + widthSqrSize, posY);
    turtle0.goto(posX + widthSqrSize, posY + heightSqrSize);
    turtle0.goto(posX, posY + heightSqrSize);
    turtle0.goto(posX, posY);
    
    turtle0.end_fill();
    turtle0.up();

def goEraseSqr(sqrNo):
    #Go to bottom-left corner of the square
    x = (sqrNo%8) * widthSqrSize - boardWidth/2;
    y = int(sqrNo/8) * heightSqrSize - boardHeight/2;
    turtle0.goto(x, y);
    
    if((sqrNo + int(sqrNo/8)) % 2 == 0):
        turtle0.color(lightSqrColor, lightSqrColor);
    else:
        turtle0.color(darkSqrColor, darkSqrColor);
    drawSqr();
    
    turtle0.color(fontColor, darkSqrColor);

def drawPiece(sqrNo, referenceBoard, inverse, noAnim):#bool inverse, inverse board if true. bool noAnim, no animation if true
    global ttWL;
    global ttWStampIdL;
    global ttbL;
    global ttbStampIdL;
    global capturedwL;
    global capturedbL;
    
    if (inverse):
        x = 63 - sqrNo;
    else:
        x = sqrNo;
        
    if (referenceBoard[sqrNo] & blackType == whiteType):
        wLIndex = -1;
        if (referenceBoard[sqrNo] & wKingBf == wKingBf):
            wLIndex = 0;
            capturedwL[0] -= 1;
        elif (referenceBoard[sqrNo] & wPawnBf == wPawnBf):
            if (referenceBoard[sqrNo] & wL4PawnBf == wPawnBf):
                wLIndex = 1;
                capturedwL[1] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wR2PawnBf):
                wLIndex = 2;
                capturedwL[2] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wR3PawnBf):
                wLIndex = 3;
                capturedwL[3] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wR4PawnBf):
                wLIndex = 4;
                capturedwL[4] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wL4PawnBf):
                wLIndex = 5;
                capturedwL[5] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wL3PawnBf):
                wLIndex = 6;
                capturedwL[6] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wL2PawnBf):
                wLIndex = 7;
                capturedwL[7] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wLPawnBf):
                wLIndex = 8;
                capturedwL[8] -= 1;
        elif (referenceBoard[sqrNo] & wQueenBf == wQueenBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            wLIndex = 9;
            capturedwL[9] -= 1;
        elif (referenceBoard[sqrNo] & wLBishopBf == wBishopBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            wLIndex = 10;
            capturedwL[10] -= 1;
        elif (referenceBoard[sqrNo] & wLBishopBf == wLBishopBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            wLIndex = 11;
            capturedwL[11] -= 1;
        elif (referenceBoard[sqrNo] & wLKnightBf == wKnightBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            wLIndex = 12;
            capturedwL[12] -= 1;
        elif (referenceBoard[sqrNo] & wLKnightBf == wLKnightBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            wLIndex = 13;
            capturedwL[13] -= 1;
        elif (referenceBoard[sqrNo] & wLRookBf == wRookBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            wLIndex = 14;
            capturedwL[14] -= 1;
        elif (referenceBoard[sqrNo] & wLRookBf == wLRookBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            wLIndex = 15;
            capturedwL[15] -= 1;

        if (wLIndex > -1):
            ttWL[wLIndex].showturtle();
            ttWL[wLIndex].clearstamp(ttWStampIdL[wLIndex]);
            goToSqr(x, ttWL[wLIndex], noAnim);
            if (referenceBoard[sqrNo] & wPawnBf == wPawnBf):
                if (referenceBoard[sqrNo] & wQueenBf == wQueenBf):
                    ttWL[wLIndex].shape(wQueenImage);
                if (referenceBoard[sqrNo] & wKnightBf == wKnightBf):
                    ttWL[wLIndex].shape(wKnightImage);
                if (referenceBoard[sqrNo] & wRookBf == wRookBf):
                    ttWL[wLIndex].shape(wRookImage);
                if (referenceBoard[sqrNo] & wBishopBf == wBishopBf):
                    ttWL[wLIndex].shape(wBishopImage);
            ttWStampIdL[wLIndex] = ttWL[wLIndex].stamp();
            ttWL[wLIndex].hideturtle();

    if (referenceBoard[sqrNo] & blackType == blackType):
        bLIndex = -1;
        if (referenceBoard[sqrNo] & wKingBf == wKingBf):
            bLIndex = 0;
            capturedbL[0] -= 1;
        elif (referenceBoard[sqrNo] & wPawnBf == wPawnBf):
            if (referenceBoard[sqrNo] & wL4PawnBf == wPawnBf):
                bLIndex = 1;
                capturedbL[1] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wR2PawnBf):
                bLIndex = 2;
                capturedbL[2] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wR3PawnBf):
                bLIndex = 3;
                capturedbL[3] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wR4PawnBf):
                bLIndex = 4;
                capturedbL[4] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wL4PawnBf):
                bLIndex = 5;
                capturedbL[5] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wL3PawnBf):
                bLIndex = 6;
                capturedbL[6] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wL2PawnBf):
                bLIndex = 7;
                capturedbL[7] -= 1;
            elif (referenceBoard[sqrNo] & wL4PawnBf == wLPawnBf):
                bLIndex = 8;
                capturedbL[8] -= 1;
        elif (referenceBoard[sqrNo] & wQueenBf == wQueenBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            bLIndex = 9;
            capturedbL[9] -= 1;
        elif (referenceBoard[sqrNo] & wLBishopBf == wBishopBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            bLIndex = 10;
            capturedbL[10] -= 1;
        elif (referenceBoard[sqrNo] & wLBishopBf == wLBishopBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            bLIndex = 11;
            capturedbL[11] -= 1;
        elif (referenceBoard[sqrNo] & wLKnightBf == wKnightBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            bLIndex = 12;
            capturedbL[12] -= 1;
        elif (referenceBoard[sqrNo] & wLKnightBf == wLKnightBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            bLIndex = 13;
            capturedbL[13] -= 1;
        elif (referenceBoard[sqrNo] & wLRookBf == wRookBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            bLIndex = 14;
            capturedbL[14] -= 1;
        elif (referenceBoard[sqrNo] & wLRookBf == wLRookBf and referenceBoard[sqrNo] & wPawnBf != wPawnBf):
            bLIndex = 15;
            capturedbL[15] -= 1;

        if (bLIndex > -1):
            ttBL[bLIndex].showturtle();
            ttBL[bLIndex].clearstamp(ttBStampIdL[bLIndex]);
            goToSqr(x, ttBL[bLIndex], noAnim);
            if (referenceBoard[sqrNo] & wPawnBf == wPawnBf):
                if (referenceBoard[sqrNo] & wQueenBf == wQueenBf):
                    ttBL[bLIndex].shape(bQueenImage);
                if (referenceBoard[sqrNo] & wKnightBf == wKnightBf):
                    ttBL[bLIndex].shape(bKnightImage);
                if (referenceBoard[sqrNo] & wRookBf == wRookBf):
                    ttBL[bLIndex].shape(bRookImage);
                if (referenceBoard[sqrNo] & wBishopBf == wBishopBf):
                    ttBL[bLIndex].shape(bBishopImage);
            ttBStampIdL[bLIndex] = ttBL[bLIndex].stamp();
            ttBL[bLIndex].hideturtle();

    
def refreshBoard(inverse, referenceBoard, noAnim):#bool inverse, inverse board if true. bool noAnim, no animation if true 
    global ttWL;
    global ttWStampIdL;
    global ttbL;
    global ttbStampIdL;
    global capturedwL;
    global capturedbL;

    capturedwL = [x + 1 for x in capturedwL];
    capturedbL = [x + 1 for x in capturedbL];

    if (inverse):
        for x in range(0,64):
            drawPiece(x, referenceBoard, inverse, noAnim);
    else:
        for x in range(63, -1, -1):
            drawPiece(x, referenceBoard, inverse, noAnim);

    for x in range(len(capturedwL)):
        if (capturedwL[x] == 1):
            ttWL[x].clearstamp(ttWStampIdL[x]);
        if (capturedbL[x] == 1):
            ttBL[x].clearstamp(ttBStampIdL[x]);
            
        
    turtle.update();
    
def transformCharCoord(char):
    
    if (char == "a"):
        return 1;
    elif (char == "b"):
        return 2;
    elif (char == "c"):
        return 3;
    elif (char == "d"):
        return 4;
    elif (char == "e"):
        return 5;
    elif (char == "f"):
        return 6;
    elif (char == "g"):
        return 7;
    elif (char == "h"):
        return 8;
    if (char == 1):
        return "a";
    elif (char == 2):
        return "b";
    elif (char == 3):
        return "c";
    elif (char == 4):
        return "d";
    elif (char == 5):
        return "e";
    elif (char == 6):
        return "f";
    elif (char == 7):
        return "g";
    elif (char == 8):
        return "h";
    
    else:
        return 0;

#Do not return anything, list address is used!
def createNestedLists(tlist, listLength):
    for _ in range(listLength):
        tlist.append([]);


#Only use hiddenTerritory and iMTAllyInRange after looping all board square for identifyMoveTrack() and the lists are cleared
def identifyMoveTrack(sqrNo, referenceBoard):
    global hiddenTerritory;
    global iMTAllyInRange;
    #print("identifyMoveTrack() called");
    pieceColor = (referenceBoard[sqrNo] & blackType);
    #print("pieceColor =", pieceColor);
    pieceX = sqrNo % 8;
    pieceY = int(sqrNo / 8);
    rectSqrNumBelow = pieceY * 8;
    moveTrack = [];
    
    if ((wRookBf & referenceBoard[sqrNo]) == wRookBf):
        #print("Rook checked")
        
        rUpY = int(sqrNo / 8);
        while (rUpY < 7):
            rUpY += 1;
            #print(rUpY);
            #Check if the upper square has no piece or has an enemy piece
            if (referenceBoard[pieceX + (rUpY * 8)] == 0):
                moveTrack.append(pieceX + (rUpY * 8));
                #print("Up track passes");
            elif ((referenceBoard[pieceX + (rUpY * 8)] & blackType) != pieceColor):
                moveTrack.append(pieceX + (rUpY * 8));
                #print("Up track passes");
                break
            elif ((referenceBoard[pieceX + (rUpY * 8)] & blackType) == pieceColor):
                iMTAllyInRange[pieceX + (rUpY * 8)].append(sqrNo);
                #print("Up track blocked");
                break;
            
        rDownY = int(sqrNo / 8);
        while (rDownY > 0):
            rDownY -= 1;
            if (referenceBoard[pieceX + (rDownY * 8)] == 0):
                moveTrack.append(pieceX + (rDownY * 8));
                #print("Down track passes");
            elif ((referenceBoard[pieceX + (rDownY * 8)] & blackType) != pieceColor):
                moveTrack.append(pieceX + (rDownY * 8));
                #print("Down track passes");
                break;
            elif ((referenceBoard[pieceX + (rDownY * 8)] & blackType) == pieceColor):
                iMTAllyInRange[pieceX + (rDownY * 8)].append(sqrNo);
                #print("Down track blocked");
                break;
        rLeftX = int(sqrNo % 8);
        while (rLeftX > 0):
            rLeftX -= 1;
            if (referenceBoard[rectSqrNumBelow + rLeftX] == 0):
                moveTrack.append(rectSqrNumBelow + rLeftX);
                #print("Left track passes");
            elif ((referenceBoard[rectSqrNumBelow + rLeftX] & blackType) != pieceColor):
                moveTrack.append(rectSqrNumBelow + rLeftX);
                #print("Left track passes");
                break;
            elif ((referenceBoard[rectSqrNumBelow + rLeftX] & blackType) == pieceColor):
                iMTAllyInRange[rectSqrNumBelow + rLeftX].append(sqrNo);
                #print("Left track blocked");
                break;
        rRightX = int(sqrNo % 8);
        while (rRightX < 7):
            rRightX += 1;
            if (referenceBoard[rectSqrNumBelow + rRightX] == 0):
                moveTrack.append(rectSqrNumBelow + rRightX);
                #print("Right track passes");
            elif ((referenceBoard[rectSqrNumBelow + rRightX] & blackType) != pieceColor):
                moveTrack.append(rectSqrNumBelow + rRightX);
                #print("Right track passes");
                break;
            elif ((referenceBoard[rectSqrNumBelow + rRightX] & blackType) == pieceColor):
                iMTAllyInRange[rectSqrNumBelow + rRightX].append(sqrNo);
                #print("Right track blocked");
                break;
#Pending: Promotion and En passant
    if ((referenceBoard[sqrNo] & pawnPrmChk) == wPawnBf):
        #print("Pawn checked")
        
        pUpY = int(sqrNo / 8);
        pawnFdRtrt = 2;
        
        if (referenceBoard[sqrNo] & blackType == whiteType):
            if (pieceY > 1):
                pawnFdRtrt = 1;
            while (pUpY < 7 and pUpY - pieceY < pawnFdRtrt):
                pUpY += 1;
                #print(pUpY);
                #Check if the upper square has no piece //or has an enemy piece
                if (referenceBoard[pieceX + (pUpY * 8)] == 0):
                    moveTrack.append(pieceX + (pUpY * 8));
                    #print("Up track passes");
                #elif ((referenceBoard[pieceX + (pUpY * 8)] & blackType) != pieceColor):
                   # print("Up track blocked");
                   # break
                else:
                   # print("Up track blocked");
                    break;
                
            #Check if the upper-left square has an enemy piece
            if (pieceX > 0 and pieceY < 7):
                if (referenceBoard[sqrNo + 7] > 0):
                    if (referenceBoard[sqrNo + 7] & blackType != pieceColor):
                        moveTrack.append(sqrNo + 7);
                        #print("Upper-left track passes");
                    else:
                        iMTAllyInRange[sqrNo + 7].append(sqrNo);
                else:
                    hiddenTerritory[sqrNo + 7].append(sqrNo);
                    
                        
            #Check if the upper-right square has an enemy piece
            if (pieceX < 7 and pieceY < 7):
                if (referenceBoard[sqrNo + 9] > 0):
                    if (referenceBoard[sqrNo + 9] & blackType != pieceColor):
                        moveTrack.append(sqrNo + 9);
                        #print("Upper-right track passes");
                    else:
                        iMTAllyInRange[sqrNo + 9].append(sqrNo);
                else:
                    hiddenTerritory[sqrNo + 9].append(sqrNo);
            
        elif (referenceBoard[sqrNo] & blackType == blackType):
            if (pieceY < 6):
                pawnFdRtrt = 1;
            while (pUpY > 0 and pieceY - pUpY< pawnFdRtrt):
                pUpY -= 1;
                #print(pUpY);
                #Check if the upper square has no piece //or has an enemy piece
                if (referenceBoard[pieceX + (pUpY * 8)] == 0):
                    moveTrack.append(pieceX + (pUpY * 8));
                    #print("Up track passes");
                #elif ((referenceBoard[pieceX + (pUpY * 8)] & blackType) != pieceColor):
                   # print("Up track blocked");
                   # break
                else:
                    #print("Up track blocked");
                    break;
                
            #Check if the upper-left square has an enemy piece
            if (pieceX < 7 and pieceY > 0):
                if (referenceBoard[sqrNo - 7] > 0):
                    if (referenceBoard[sqrNo - 7] & blackType != pieceColor):
                        moveTrack.append(sqrNo - 7);
                        #print("Upper-left track passes");
                    else:
                        iMTAllyInRange[sqrNo - 7].append(sqrNo);
                else:
                    hiddenTerritory[sqrNo - 7].append(sqrNo);
                        
            #Check if the upper-right square has an enemy piece
            if (pieceX > 0 and pieceY > 0):
                if (referenceBoard[sqrNo - 9] > 0):
                    if (referenceBoard[sqrNo - 9] & blackType != pieceColor):
                        moveTrack.append(sqrNo - 9);
                        #print("Upper-right track passes");
                    else:
                        iMTAllyInRange[sqrNo - 9].append(sqrNo);
                else:
                    hiddenTerritory[sqrNo - 9].append(sqrNo);
                        
                    
    if ((wBishopBf & referenceBoard[sqrNo]) == wBishopBf):
        #print("Bishop checked")
        
        #Check upper-left track
        bUpLY = int(sqrNo / 8);
        bUpLX = pieceX;
        while (bUpLY < 7 and bUpLX > 0):
            
            bUpLY += 1;
            bUpLX -= 1;
            
            if (referenceBoard[bUpLY * 8 + bUpLX] == 0):
                moveTrack.append(bUpLY * 8 + bUpLX);
                #print("Upper-left track passes");
            elif ((referenceBoard[bUpLY * 8 + bUpLX] & blackType) != pieceColor):
                moveTrack.append(bUpLY * 8 + bUpLX);
                break;
            else:
                iMTAllyInRange[bUpLY * 8 + bUpLX].append(sqrNo);
                #print("Upper-left track blocked");
                break;
        #Check upper-right track
        bUpRY = int(sqrNo / 8);
        bUpRX = pieceX;
        while (bUpRY < 7 and bUpRX < 7):
            
            bUpRY += 1;
            bUpRX += 1;
            
            if (referenceBoard[bUpRY * 8 + bUpRX] == 0):
                moveTrack.append(bUpRY * 8 + bUpRX);
                #print("Upper-right track passes");
            elif ((referenceBoard[bUpRY * 8 + bUpRX] & blackType) != pieceColor):
                moveTrack.append(bUpRY * 8 + bUpRX);
                break;
            else:
                iMTAllyInRange[bUpRY * 8 + bUpRX].append(sqrNo);
                #print("Upper-right track blocked");
                break;
        #Check bottom-left track
        bBLY = int(sqrNo / 8);
        bBLX = pieceX;
        while (bBLY > 0 and bBLX > 0):
            
            bBLY -= 1;
            bBLX -= 1;
            
            if (referenceBoard[bBLY * 8 + bBLX] == 0):
                moveTrack.append(bBLY * 8 + bBLX);
                #print("Bottom-left track passes");
            elif ((referenceBoard[bBLY * 8 + bBLX] & blackType) != pieceColor):
                moveTrack.append(bBLY * 8 + bBLX);
                break;
            else:
                iMTAllyInRange[bBLY * 8 + bBLX].append(sqrNo);
                #print("Bottom-left track blocked");
                break;
            
        #Check bottom-right track
        bBRY = int(sqrNo / 8);
        bBRX = pieceX;
        while (bBRY > 0 and bBRX < 7):
            
            bBRY -= 1;
            bBRX += 1;
            
            if (referenceBoard[bBRY * 8 + bBRX] == 0):
                moveTrack.append(bBRY * 8 + bBRX);
                #print("Bottom-right track passes");
            elif ((referenceBoard[bBRY * 8 + bBRX] & blackType) != pieceColor):
                moveTrack.append(bBRY * 8 + bBRX);
                break;
            else:
                iMTAllyInRange[bBRY * 8 + bBRX].append(sqrNo);
                #print("Bottom-right track blocked");
                break;
 
    if ((wKnightBf & referenceBoard[sqrNo]) == wKnightBf):
        #print("Knight checked")
        #Check upper-left track            
        if (pieceY < 6 and pieceX > 0):
            if ((referenceBoard[sqrNo + 15] == 0) or ((referenceBoard[sqrNo + 15] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 15);
                #print("Upper-left track passes");
            else:
                iMTAllyInRange[sqrNo + 15].append(sqrNo);
                #print("Upper-left track blocked");
        #Check left-up track            
        if (pieceY < 7 and pieceX > 1):
            if ((referenceBoard[sqrNo + 6] == 0) or ((referenceBoard[sqrNo + 6] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 6);
                #print("Left-up track passes");
            else:
                iMTAllyInRange[sqrNo + 6].append(sqrNo);
                #print("Left-up track blocked");
                #Check upper-right track            
        if (pieceY < 6 and pieceX < 7):
            if ((referenceBoard[sqrNo + 17] == 0) or ((referenceBoard[sqrNo + 17] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 17);
                #print("Upper-right track passes");
            else:
                iMTAllyInRange[sqrNo + 17].append(sqrNo);
                #print("Upper-right track blocked");
        #Check right-up track            
        if (pieceY < 7 and pieceX < 6):
            if ((referenceBoard[sqrNo + 10] == 0) or ((referenceBoard[sqrNo + 10] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 10);
                #print("Right-up track passes");
            else:
                iMTAllyInRange[sqrNo + 10].append(sqrNo);
                #print("Right-up track blocked");
        #Check bottom-left track            
        if (pieceY > 1 and pieceX > 0):
            if ((referenceBoard[sqrNo - 17] == 0) or ((referenceBoard[sqrNo - 17] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 17);
                #print("Bottom-left track passes");
            else:
                iMTAllyInRange[sqrNo - 17].append(sqrNo);
                #print("Bottom-left track blocked");
        #Check left-bottom track            
        if (pieceY > 0 and pieceX > 1):
            if ((referenceBoard[sqrNo - 10] == 0) or ((referenceBoard[sqrNo - 10] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 10);
                #print("Left-bottom track passes");
            else:
                iMTAllyInRange[sqrNo - 10].append(sqrNo);
                #print("Left-bottom track blocked");
        #Check bottom-right track            
        if (pieceY > 1 and pieceX < 7):
            if ((referenceBoard[sqrNo - 15] == 0) or ((referenceBoard[sqrNo - 15] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 15);
                #print("Bottom-right track passes");
            else:
                iMTAllyInRange[sqrNo - 15].append(sqrNo);
                #print("Bottom-right track blocked");
        #Check right-bottom track            
        if (pieceY > 0 and pieceX < 6):
            if ((referenceBoard[sqrNo - 6] == 0) or ((referenceBoard[sqrNo - 6] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 6);
                #print("Right-bottom track passes");
            else:
                iMTAllyInRange[sqrNo - 6].append(sqrNo);
                #print("Right-bottom track blocked");
    if ((wQueenBf & referenceBoard[sqrNo]) == wQueenBf):
        #print("Queen checked")
        
        qUpY = int(sqrNo / 8);
        while (qUpY < 7):
            qUpY += 1;
            #print(qUpY);
            #Check if the upper square has no piece or has an enemy piece
            if (referenceBoard[pieceX + (qUpY * 8)] == 0):
                moveTrack.append(pieceX + (qUpY * 8));
                #print("Up track passes");
            elif ((referenceBoard[pieceX + (qUpY * 8)] & blackType) != pieceColor):
                moveTrack.append(pieceX + (qUpY * 8));
                #print("Up track passes");
                break
            else:
                iMTAllyInRange[pieceX + (qUpY * 8)].append(sqrNo);
                #print("Up track blocked");
                break;
            
        qDownY = int(sqrNo / 8);
        while (qDownY > 0):
            qDownY -= 1;
            if (referenceBoard[pieceX + (qDownY * 8)] == 0):
                moveTrack.append(pieceX + (qDownY * 8));
                #print("Down track passes");
            elif ((referenceBoard[pieceX + (qDownY * 8)] & blackType) != pieceColor):
                moveTrack.append(pieceX + (qDownY * 8));
                #print("Down track passes");
                break;
            else:
                iMTAllyInRange[pieceX + (qDownY * 8)].append(sqrNo);
                #print("Down track blocked");
                break;
        qLeftX = int(sqrNo % 8);
        while (qLeftX > 0):
            qLeftX -= 1;
            if (referenceBoard[rectSqrNumBelow + qLeftX] == 0):
                moveTrack.append(rectSqrNumBelow + qLeftX);
                #print("Left track passes");
            elif ((referenceBoard[rectSqrNumBelow + qLeftX] & blackType) != pieceColor):
                moveTrack.append(rectSqrNumBelow + qLeftX);
                #print("Left track passes");
                break;
            else:
                iMTAllyInRange[rectSqrNumBelow + qLeftX].append(sqrNo);
                #print("Left track blocked");
                break;
            
        qRightX = int(sqrNo % 8);
        while (qRightX < 7):
            qRightX += 1;
            if (referenceBoard[rectSqrNumBelow + qRightX] == 0):
                moveTrack.append(rectSqrNumBelow + qRightX);
                #print("Right track passes");
            elif ((referenceBoard[rectSqrNumBelow + qRightX] & blackType) != pieceColor):
                moveTrack.append(rectSqrNumBelow + qRightX);
                #print("Right track passes");
                break;
            else:
                iMTAllyInRange[rectSqrNumBelow + qRightX].append(sqrNo);
                #print("Right track blocked");
                break;
            
        #Check upper-left track
        qUpLY = int(sqrNo / 8);
        qUpLX = pieceX;
        while (qUpLY < 7 and qUpLX > 0):
            
            qUpLY += 1;
            qUpLX -= 1;
            
            if (referenceBoard[qUpLY * 8 + qUpLX] == 0):
                moveTrack.append(qUpLY * 8 + qUpLX);
                #print("Upper-left track passes");
            elif ((referenceBoard[qUpLY * 8 + qUpLX] & blackType) != pieceColor):
                moveTrack.append(qUpLY * 8 + qUpLX);
                break;
            else:
                iMTAllyInRange[qUpLY * 8 + qUpLX].append(sqrNo);
                #print("Upper-left track blocked");
                break;
        #Check upper-right track
        qUpRY = int(sqrNo / 8);
        qUpRX = pieceX;
        while (qUpRY < 7 and qUpRX < 7):
            
            qUpRY += 1;
            qUpRX += 1;
            
            if (referenceBoard[qUpRY * 8 + qUpRX] == 0):
                moveTrack.append(qUpRY * 8 + qUpRX);
                #print("Upper-right track passes");
            elif ((referenceBoard[qUpRY * 8 + qUpRX] & blackType) != pieceColor):
                moveTrack.append(qUpRY * 8 + qUpRX);
                break;
            else:
                iMTAllyInRange[qUpRY * 8 + qUpRX].append(sqrNo);
                #print("Upper-right track blocked");
                break;
        #Check bottom-left track
        qBLY = int(sqrNo / 8);
        qBLX = pieceX;
        while (qBLY > 0 and qBLX > 0):
            
            qBLY -= 1;
            qBLX -= 1;
            
            if (referenceBoard[qBLY * 8 + qBLX] == 0):
                moveTrack.append(qBLY * 8 + qBLX);
                #print("Bottom-left track passes");
            elif ((referenceBoard[qBLY * 8 + qBLX] & blackType) != pieceColor):
                moveTrack.append(qBLY * 8 + qBLX);
                break;
            else:
                iMTAllyInRange[qBLY * 8 + qBLX].append(sqrNo);
                #print("Bottom-left track blocked");
                break;
        #Check bottom-right track
        qBRY = int(sqrNo / 8);
        qBRX = pieceX;
        while (qBRY > 0 and qBRX < 7):
            
            qBRY -= 1;
            qBRX += 1;
            
            if (referenceBoard[qBRY * 8 + qBRX] == 0):
                moveTrack.append(qBRY * 8 + qBRX);
                #print("Bottom-right track passes");
            elif ((referenceBoard[qBRY * 8 + qBRX] & blackType) != pieceColor):
                moveTrack.append(qBRY * 8 + qBRX);
                break;
            else:
                iMTAllyInRange[qBRY * 8 + qBRX].append(sqrNo);
                #print("Bottom-right track blocked");
                break;
    
    if ((wKingBf & referenceBoard[sqrNo]) == wKingBf):
        #print("King checked")
        #Check upper track            
        if (pieceY < 7):
            if ((referenceBoard[sqrNo + 8] == 0) or ((referenceBoard[sqrNo + 8] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 8);
                #print("Upper track passes");
            #else:
                #print("Upper track blocked");
        #Check bottom track            
        if (pieceY > 0):
            if ((referenceBoard[sqrNo - 8] == 0) or ((referenceBoard[sqrNo - 8] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 8);
                #print("Bottom track passes");
            #else:
                #print("Bottom track blocked");
        #Check left track            
        if (pieceX > 0):
            if ((referenceBoard[sqrNo - 1] == 0) or ((referenceBoard[sqrNo - 1] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 1);
                #print("Left track passes");
            #else:
                #print("Left track blocked");
        #Check right track            
        if (pieceX < 7):
            if ((referenceBoard[sqrNo + 1] == 0) or ((referenceBoard[sqrNo + 1] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 1);
                #print("Right track passes");
            #else:
                #print("Right track blocked");
        #Check upper-left track            
        if (pieceY < 7 and pieceX > 0):
            if ((referenceBoard[sqrNo + 7] == 0) or ((referenceBoard[sqrNo + 7] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 7);
                #print("Upper-left track passes");
            #else:
                #print("Upper-left track blocked");
        #Check upper-right track            
        if (pieceY < 7 and pieceX < 7):
            if ((referenceBoard[sqrNo + 9] == 0) or ((referenceBoard[sqrNo + 9] & blackType) != pieceColor)):
                moveTrack.append(sqrNo + 9);
                #print("Upper-right track passes");
            #else:
                #print("Upper-right track blocked");
        #Check bottom-left track            
        if (pieceY > 0 and pieceX > 0):
            if ((referenceBoard[sqrNo - 9] == 0) or ((referenceBoard[sqrNo - 9] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 9);
                #print("Bottom-left track passes");
            #else:
                #print("Bottom-left track blocked");
        #Check bottom-right track            
        if (pieceY > 0 and pieceX < 7):
            if ((referenceBoard[sqrNo - 7] == 0) or ((referenceBoard[sqrNo - 7] & blackType) != pieceColor)):
                moveTrack.append(sqrNo - 7);
                #print("Bottom-right track passes");
            #else:
                #print("Bottom-right track blocked");
    #print(moveTrack);
    return moveTrack;
    
 
#Pending machine lerning
availableMoveIndex = 0.001;#Additional value of each move available
territoryValueIndex = 0.05;#Value of each accessable square by the same color
pawnValueIndex = 1;
rookValueIndex = 5;
bishopValueIndex = 3;
knightValueIndex = 3;
queenValueIndex = 9;
kingValueIndex = 10;
defendValueIndex = 0.001;#Multiply by piece value
attackValueIndex = 0.003;#Multiply by piece value
def valueIndexUpdate():
    #Determine the average territory occupied by each piece, change percentage to avg in the beginning and end play
    #Bonus for protection and capture
    #Special Bonus for King protection and capture
    cont = 0;

def identifyPieceValue(sqrBf):
    if(sqrBf & pawnPrmChk == wPawnBf):
        return pawnValueIndex;    
    elif(sqrBf & wBishopBf == wBishopBf):
        return bishopValueIndex;  
    elif(sqrBf & wKnightBf == wKnightBf):
        return knightValueIndex;  
    elif(sqrBf & wRookBf == wRookBf):
        return rookValueIndex;  
    elif(sqrBf & wQueenBf == wQueenBf):
        return queenValueIndex;
    elif(sqrBf & wKingBf == wKingBf):
        return kingValueIndex;

#Calculate moveValue
def moveValueCalculation(referenceBoard, ColorBf, turnsSimulated):
    global iMTAllyInRange;
    global hiddenTerritory;
    moveValue = 0;#default
    
    #AI data initialization
    boardCdt = [0] * 64;#Bitflags for square condition
    possibleMmT = [];#All moves avilable in the lists of (startSqr, endSqr);
    boardSqrInRange = [];
    createNestedLists(boardSqrInRange, 64);
    
    #AI: Calculate data
    iMTAllyInRange = [];#Set global at top of the function
    createNestedLists(iMTAllyInRange, 64);
    hiddenTerritory = [];#Set global at top of the function
    createNestedLists(hiddenTerritory, 64);
    for x in range(64):
        if (referenceBoard[x] > 0):
            moveTrack = identifyMoveTrack(x, referenceBoard);
            if (referenceBoard[x] & pawnPrmChk != wPawnBf):
                for y in moveTrack:
                    #print("Square", y, "is in the range of piece at square", x);
                    z = [x];#Turn x to a list for list merging
                    boardSqrInRange[y].extend(z);
                    
                    if(referenceBoard[x] & blackType == whiteType):
                        boardCdt[y] = wTerritory | boardCdt[y];
                    else:
                        boardCdt[y] = bTerritory | boardCdt[y];
                   
            if (referenceBoard[x] & blackType == ColorBf):
                for i in range(len(moveTrack)):
                    tempBoard = [x, moveTrack[i]];
                    possibleMmT.append(tempBoard);

    for x in range(64):
        if (referenceBoard[x] > 0):        
            if(referenceBoard[x] & blackType == whiteType and len(iMTAllyInRange[x]) > 0):
                boardCdt[x] = wTerritory | boardCdt[x];
            elif (referenceBoard[x] & blackType == blackType and len(iMTAllyInRange[x]) > 0):
                boardCdt[x] = bTerritory | boardCdt[x];
        if (len(hiddenTerritory[x]) > 0):
            for y in hiddenTerritory[x]:
                if (referenceBoard[y] & blackType == whiteType):
                    boardCdt[x] = wTerritory | boardCdt[x];
                else:
                    boardCdt[x] = bTerritory | boardCdt[x];
                if (referenceBoard[y] & pawnPrmChk == wPawnBf):
                    boardSqrInRange[x].append(y);

    for x in range(64):
        if (referenceBoard[x] > 0):
            trapValue = 0;#To be subtracted from move value
            defendValue = 0;
            attackValue = 0;
            oppDefValue = 0;
            #Check if piece is in enemy's range
            if (boardCdt[x] & mixedTerritory != zeroCdt):
                if (referenceBoard[x] & blackType == ColorBf):
                    #Trap value and defend value
                    if (referenceBoard[x] & blackType == whiteType):
                        if (boardCdt[x] & mixedTerritory == wTerritory):
                            defendValue += identifyPieceValue(referenceBoard[x]) * defendValueIndex;
                        elif (boardCdt[x] & mixedTerritory == bTerritory):
                                if (referenceBoard[x] & wKingBf == wKingBf and turnsSimulated == 1):
                                    trapValue -= baseValue;#Double negative for baseValue
                                else:
                                    trapValue += identifyPieceValue(referenceBoard[x]);
                    else:
                        if (boardCdt[x] & mixedTerritory == bTerritory):
                            defendValue += identifyPieceValue(referenceBoard[x]) * defendValueIndex;
                        elif (boardCdt[x] & mixedTerritory == wTerritory):
                                if (referenceBoard[x] & wKingBf == wKingBf and turnsSimulated == 1):
                                    trapValue -= baseValue;
                                else:
                                    trapValue += identifyPieceValue(referenceBoard[x]);
                else:
                    #Attack value and opposite side defend value
                    if (referenceBoard[x] & blackType == whiteType):
                        if (boardCdt[x] & mixedTerritory == wTerritory):
                            oppDefValue += identifyPieceValue(referenceBoard[x]) * defendValueIndex;
                        elif (boardCdt[x] & mixedTerritory == bTerritory):
                                attackValue += identifyPieceValue(referenceBoard[x]) * attackValueIndex;
                                
                    else:
                        if (boardCdt[x] & mixedTerritory == bTerritory):
                            oppDefValue += identifyPieceValue(referenceBoard[x]) * defendValueIndex;
                        elif (boardCdt[x] & mixedTerritory == wTerritory):
                                attackValue += identifyPieceValue(referenceBoard[x]) * attackValueIndex;
    
                #Check if piece is in enemy's range with protection
                if (boardCdt[x] & mixedTerritory == mixedTerritory):
                    allyValueInRange = [];
                    enemyValueInRange = [];
                    for y in iMTAllyInRange[x]:
                        allyValueInRange.append(identifyPieceValue(referenceBoard[y]));
                    for y in boardSqrInRange[x]:#It is the same as all enemies in range as ally piece cannot step on ally pieces
                        enemyValueInRange.append(identifyPieceValue(referenceBoard[y]));

                    if (referenceBoard[x] & blackType == ColorBf):
                        if (referenceBoard[x] & wKingBf == wKingBf and turnsSimulated == 1):
                            mixedTrapValue = -baseValue;
                        else:
                            mixedTrapValue = identifyPieceValue(referenceBoard[x]);     
                        while (len(allyValueInRange) > 0 and len(enemyValueInRange) > 0):
                            mixedTrapValue -= min(enemyValueInRange);
                            enemyValueInRange.remove(min(enemyValueInRange));
                            if (len(enemyValueInRange) > 0):
                                mixedTrapValue += min(allyValueInRange);
                                allyValueInRange.remove(min(allyValueInRange));
                        if (mixedTrapValue > 0):
                            trapValue += mixedTrapValue;
                    
                    else:
                        attackValue += identifyPieceValue(referenceBoard[x]) * attackValueIndex;       
                        while (len(allyValueInRange) > 0 and len(enemyValueInRange) > 0):
                            attackValue -= min(enemyValueInRange) * attackValueIndex;
                            enemyValueInRange.remove(min(enemyValueInRange));
                            if (len(enemyValueInRange) > 0):
                                attackValue += min(allyValueInRange) * attackValueIndex;
                                allyValueInRange.remove(min(allyValueInRange));
                    
                #trapValue should not add value to moveValue as enemy piece will not move in disadvantages
                if (trapValue < 0):
                    trapValue = 0;
                #Ally piece will not attack in disadvantage
                if (attackValue < 0):
                    attackValue = 0;
                
                moveValue += (defendValue + attackValue - oppDefValue - trapValue);
                #print(moveValue, defendValue, attackValue, oppDefValue, trapValue)
                
    for x in range(64):
        if(referenceBoard[x] > 0):
            #Survive value
            if (referenceBoard[x] & blackType == ColorBf):
                if (referenceBoard[x] & wKingBf != wKingBf):
                    moveValue += identifyPieceValue(referenceBoard[x]);
                elif (referenceBoard[x] & wKingBf == wKingBf):
                    moveValue -= baseValue;#Double negative for baseValue
            else:
                if (referenceBoard[x] & wKingBf != wKingBf):
                    moveValue -= identifyPieceValue(referenceBoard[x]);
                elif (referenceBoard[x] & wKingBf == wKingBf):
                    moveValue += baseValue;#baseValue is negative
                
            #Territory value
            if ((ColorBf == whiteType and (boardCdt[x] & mixedTerritory == wTerritory))\
                or (ColorBf == blackType and (boardCdt[x] & mixedTerritory == bTerritory))):
                moveValue += territoryValueIndex;
            elif ((ColorBf == whiteType and (boardCdt[x] & mixedTerritory == bTerritory))\
                or (ColorBf == blackType and (boardCdt[x] & mixedTerritory == wTerritory))):
                moveValue -= territoryValueIndex;

    #Available move value
    moveValue += len(possibleMmT) * availableMoveIndex;
    
    #if (moveValue > 18):
        #print(boardCdt);
        #print(iMTAllyInRange);
        #print(hiddenTerritory);
        #refreshBoard(0, referenceBoard, 0);
        #while(1):
            #cont = 1;
    return moveValue;

def moveInfoList():
    return [wKingMoved, bKingMoved, wLRookMoved, wRRookMoved, bLRookMoved, bRRookMoved];

def movementTrack(referenceBoard, currentColorBf, infoList, Rank2FdPawnSqr):
    global hiddenTerritory;
    
    #local scope for below var
    wKingMoved = infoList[0];
    bKingMoved = infoList[1];
    wLRookMoved = infoList[2];
    wRRookMoved = infoList[3];
    bLRookMoved = infoList[4];
    bRRookMoved = infoList[5];
    
    possibleMmT = [];#All moves avilable in the lists of (startSqr, endSqr)
    kingChecked = 0;#Check if own king is checked
    enemySqrInRange = [];#Only for enemies in range
    createNestedLists(enemySqrInRange, 64);
    hiddenTerritory = [];#Set global at top of the function
    createNestedLists(hiddenTerritory, 64);
    posCastlingMmT = [[4, 2], [60, 58], [4,6], [60,62]];
    
    #AI: refresh data
    for x in range(0,64):
        if (referenceBoard[x] > 0):
            moveTrack = identifyMoveTrack(x, referenceBoard);
            if (referenceBoard[x] & blackType == currentColorBf):
                for i in range(len(moveTrack)):
                    #Check is promotion is available
                    #The only possible move for having 3 elements in the nested list in possibleMmT
                    #and the startSqr is a pawn type is promotion
                    #possibleMmT[i][2]: 0 is queen, 1 is knight, 2 is rook, 3 is bishop
                    if ((referenceBoard[x] & pawnPrmChk == wPawnBf and referenceBoard[x] & blackType == whiteType and moveTrack[i] / 8 >= 7)\
                        or (referenceBoard[x] & pawnPrmChk == wPawnBf and referenceBoard[x] & blackType == blackType and int(moveTrack[i] / 8) < 1)):
                        possibleMmT.extend([[x, moveTrack[i], 0], [x, moveTrack[i], 1], [x, moveTrack[i], 2], [x, moveTrack[i], 3]]);
                    else:
                        tempMove = [x, moveTrack[i]];
                        possibleMmT.append(tempMove);
            #Check if castling is available
            if ((currentColorBf == whiteType and wKingMoved == 0 and (wLRookMoved == 0 or wRRookMoved == 0))\
                or (currentColorBf == blackType and bKingMoved == 0 and (bLRookMoved == 0 or bRRookMoved == 0))):
                if (referenceBoard[x] & currentColorBf != currentColorBf):
                    if (referenceBoard[x] & pawnPrmChk != wPawnBf):
                        for y in moveTrack:
                            #print("Square", y, "is in the range of piece at square", x);
                            enemySqrInRange[y].append(x);
                                                
    for x in range(64):
        if (len(hiddenTerritory[x]) > 0):
            for y in hiddenTerritory[x]:
                if (referenceBoard[y] & pawnPrmChk == wPawnBf):
                    enemySqrInRange[x].append(y);
                    #print("enemySqrInRange:", y, x);
                    if ((x - 8 == Rank2FdPawnSqr and referenceBoard[y] & blackType == whiteType\
                         and referenceBoard[Rank2FdPawnSqr] & blackType == blackType)\
                        or (x + 8 == Rank2FdPawnSqr and referenceBoard[y] & blackType == blackType\
                            and referenceBoard[Rank2FdPawnSqr] & blackType == whiteType)):
                        possibleMmT.append([y, x]);
                        print(hiddenTerritory);
                        print("EN passant:", y, x);
                            
    #Check if castling is available
    #The only possible move for king moving in castling square
    #and a rook of the same side is present in the castling square in possibleMmT is castling 
    if ((currentColorBf == whiteType and wKingMoved == 0 and (wLRookMoved == 0 or wRRookMoved == 0))\
        or (currentColorBf == blackType and bKingMoved == 0 and (bLRookMoved == 0 or bRRookMoved == 0))):
        for x in range(64):
            if (referenceBoard[x] & wKingBf == wKingBf and referenceBoard[x] & currentColorBf == currentColorBf\
                and len(enemySqrInRange[x]) > 0):
               kingChecked = 1;
        if (kingChecked == 0):  
            for i in range(len(posCastlingMmT)):
                if (((posCastlingMmT[i][0] == 4 and posCastlingMmT[i][1] == 2) or (posCastlingMmT[i][0] == 60 and posCastlingMmT[i][1] == 58))\
                    and len(enemySqrInRange[posCastlingMmT[i][0] - 1]) == 0 and len(enemySqrInRange[posCastlingMmT[i][0] - 2]) == 0 and len(enemySqrInRange[posCastlingMmT[i][0] - 3]) == 0\
                    and referenceBoard[posCastlingMmT[i][0] - 1] == 0 and referenceBoard[posCastlingMmT[i][0] - 2] == 0 and referenceBoard[posCastlingMmT[i][0] - 3] == 0):
                    if (posCastlingMmT[i][0] == 4 and posCastlingMmT[i][1] == 2\
                        and referenceBoard[posCastlingMmT[i][0]] & bKingBf == wKingBf and referenceBoard[0] & bLRookBf == wLRookBf and referenceBoard[0] & wPawnBf != wPawnBf\
                        and wKingMoved == 0 and wLRookMoved == 0):
                        possibleMmT.append([4, 2]);
                    elif (posCastlingMmT[i][0] == 60 and posCastlingMmT[i][1] == 58\
                        and referenceBoard[posCastlingMmT[i][0]] & bKingBf == bKingBf and referenceBoard[56] & bLRookBf == bRookBf and referenceBoard[56] & wPawnBf != wPawnBf\
                        and bKingMoved == 0 and bRRookMoved == 0):
                        possibleMmT.append([60, 58]);
                elif (((posCastlingMmT[i][0] == 4 and posCastlingMmT[i][1] == 6) or (posCastlingMmT[i][0] == 60 and posCastlingMmT[i][1] == 62))\
                    and len(enemySqrInRange[posCastlingMmT[i][0] + 1]) == 0 and len(enemySqrInRange[posCastlingMmT[i][0] + 2]) == 0\
                    and referenceBoard[posCastlingMmT[i][0] + 1] == 0 and referenceBoard[posCastlingMmT[i][0] + 2] == 0):
                    if (posCastlingMmT[i][0] == 4 and posCastlingMmT[i][1] == 6\
                        and referenceBoard[posCastlingMmT[i][0]] & bKingBf == wKingBf and referenceBoard[7] & bLRookBf == wRookBf and referenceBoard[7] & wPawnBf != wPawnBf\
                        and wKingMoved == 0 and wRRookMoved == 0):
                        possibleMmT.append([4, 6]);
                    elif (posCastlingMmT[i][0] == 60 and posCastlingMmT[i][1] == 62\
                        and referenceBoard[posCastlingMmT[i][0]] & bKingBf == bKingBf and referenceBoard[63] & bLRookBf == bLRookBf and referenceBoard[63] & wPawnBf != wPawnBf\
                        and bKingMoved == 0 and bLRookMoved == 0):
                        possibleMmT.append([60, 62]);
    return possibleMmT;

def aiMoveDecide(referenceBoard, turnsSimulated, route, turnColor, checkMateTest, infoList, Rank2FdPawnSqr):#bool checkMateTest, infoList(wKingMoved, bKingMoved, wLRookMoved, wRRookMoved, bLRookMoved, bRRookMoved)
    #Local var
    turnsSimulated += 1;
    #local scope for below var
    #print("infoList:", infoList);
    wKingMoved = infoList[0];
    bKingMoved = infoList[1];
    wLRookMoved = infoList[2];
    wRRookMoved = infoList[3];
    bLRookMoved = infoList[4];
    bRRookMoved = infoList[5];
    #print(turnsSimulated);
    if(turnsSimulated > turnsToSimulate):
        print("Error: aiMoveDecide() forced out", turnsSimulated)
        return;
    if (turnsSimulated % 2 == 1):
        currentColorBf = turnColor;
    else:
        if (turnColor == whiteType):
            currentColorBf = blackType;
        else:
            currentColorBf = whiteType;
    
    #AI data
    possibleMmT = movementTrack(referenceBoard, currentColorBf, infoList, Rank2FdPawnSqr);#All moves avilable in the lists of (startSqr, endSqr)

    #Check if castling is available
    if ((currentColorBf == whiteType and wKingMoved == 0 and (wLRookMoved == 0 or wRRookMoved == 0))\
        or (currentColorBf == blackType and bKingMoved == 0 and (bLRookMoved == 0 or bRRookMoved == 0))):
        castlingBoard1 = list(referenceBoard);
        castlingBoard2 = list(referenceBoard);
        castlingInfoList1 = list(infoList);
        castlingInfoList2 = list(infoList);
        
        for i in range(len(possibleMmT)):
            if (possibleMmT[i][0] == 4 and possibleMmT[i][1] == 2\
                and referenceBoard[4] & bKingBf == wKingBf and referenceBoard[0] & bLRookBf == wLRookBf and referenceBoard[0] & wPawnBf != wPawnBf):
                castlingInfoList1[0] = 1;
                castlingInfoList1[2] = 1;
                castlingBoard1[4] = whiteType;
                castlingBoard1[0] = whiteType;
                castlingBoard1[2] = wKingBf;
                castlingBoard1[3] = wLRookBf;
                break;
            elif (possibleMmT[i][0] == 60 and possibleMmT[i][1] == 58\
                and referenceBoard[60] & bKingBf == bKingBf and referenceBoard[56] & bLRookBf == bRookBf and referenceBoard[56] & wPawnBf != wPawnBf):
                castlingInfoList2[1] = 1;
                castlingInfoList2[5] = 1;
                castlingBoard2[60] = whiteType;
                castlingBoard2[56] = whiteType;
                castlingBoard2[58] = bKingBf;
                castlingBoard2[59] = bRookBf;
                break;
            elif (possibleMmT[i][0] == 4 and possibleMmT[i][1] == 6\
                and referenceBoard[4] & bKingBf == wKingBf and referenceBoard[7] & bLRookBf == wRookBf and referenceBoard[7] & wPawnBf != wPawnBf):
                castlingInfoList2[0] = 1;
                castlingInfoList2[3] = 1;
                castlingBoard2[4] = whiteType;
                castlingBoard2[7] = whiteType;
                castlingBoard2[6] = wKingBf;
                castlingBoard2[5] = wRookBf;
                break;
            elif (possibleMmT[i][0] == 60 and possibleMmT[i][1] == 62\
                and referenceBoard[60] & bKingBf == bKingBf and referenceBoard[63] & bLRookBf == bLRookBf and referenceBoard[63] & wPawnBf != wPawnBf):
                castlingInfoList1[1] = 1;
                castlingInfoList1[4] = 1;
                castlingBoard1[60] = whiteType;
                castlingBoard1[63] = whiteType;
                castlingBoard1[62] = bKingBf;
                castlingBoard1[61] = bLRookBf;
                break;
    
    if(turnsSimulated == 1):
        global moveAdvantageL;
        moveAdvantageL = [];
        createNestedLists(moveAdvantageL, len(possibleMmT));
        for i in range(len(possibleMmT)):
            tempList = [0] * turnsToSimulate;
            moveAdvantageL[i].extend(tempList);
        #print(moveAdvantageL);
        global lastMoveValueL;
        if (turnsToSimulate != 1 and ((turnsNum == 1 and pvcCColorBf == whiteType) != 1) and checkMateTest != 1):
            lastMoveValueL = [-baseValue] * len(possibleMmT);#Ceiling value
        else:
            lastMoveValueL = [0] * len(possibleMmT);
        global initBoardValue;
        initBoardValue = moveValueCalculation(referenceBoard, currentColorBf, 0);
    
    #print(possibleMmT);#All possible moves
 
    #Iterate all possible board positions for current referenceBoard
    #Check if the piece has computer-side color and can move
    tempMoveValue = [0] * len(possibleMmT);
    for i in range(len(possibleMmT)):
        #print(possibleMmT[i][0], referenceBoard[possibleMmT[i][0]], referenceBoard[possibleMmT[i][0]] & blackType, currentColorBf)
        
        #Set new board positions
        #Check if the move is castling
        if ((possibleMmT[i][0] == 4 and possibleMmT[i][1] == 2\
            and referenceBoard[4] & bKingBf == wKingBf and referenceBoard[0] & bLRookBf == wLRookBf and referenceBoard[0] & wPawnBf != wPawnBf)\
            or (possibleMmT[i][0] == 60 and possibleMmT[i][1] == 62\
            and referenceBoard[60] & bKingBf == bKingBf and referenceBoard[63] & bLRookBf == bLRookBf and referenceBoard[63] & wPawnBf != wPawnBf)):
            tempBoard = castlingBoard1;#Assign to address
            infoList = castlingInfoList1;#Assign to address
            #print("castlingInfoList1:", infoList, "Castling move:", possibleMmT[i][0], possibleMmT[i][1]);
        elif ((possibleMmT[i][0] == 60 and possibleMmT[i][1] == 58\
            and referenceBoard[60] & bKingBf == bKingBf and referenceBoard[56] & bLRookBf == bRookBf and referenceBoard[56] & wPawnBf != wPawnBf)\
            or (possibleMmT[i][0] == 4 and possibleMmT[i][1] == 6\
            and referenceBoard[4] & bKingBf == wKingBf and referenceBoard[7] & bLRookBf == wRookBf and referenceBoard[7] & wPawnBf != wPawnBf)):
            tempBoard = castlingBoard2;#Assign to address
            infoList = castlingInfoList2;#Assign to address
            #print("castlingInfoList1:", infoList, "Castling move:", possibleMmT[i][0], possibleMmT[i][1]);
        #Check if the move is promotion
        elif (len(possibleMmT[i]) == 3 and referenceBoard[possibleMmT[i][0]] & pawnPrmChk == wPawnBf):
            if (possibleMmT[i][2] == 0):
                tempBoard = list(referenceBoard);
                tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wQueenBf;
                tempBoard[possibleMmT[i][0]] = whiteType;
            if (possibleMmT[i][2] == 1):
                tempBoard = list(referenceBoard);
                tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wKnightBf;
                tempBoard[possibleMmT[i][0]] = whiteType;
            if (possibleMmT[i][2] == 2):
                tempBoard = list(referenceBoard);
                tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wRookBf;
                tempBoard[possibleMmT[i][0]] = whiteType;
            if (possibleMmT[i][2] == 3):
                tempBoard = list(referenceBoard);
                tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wBishopBf;
                tempBoard[possibleMmT[i][0]] = whiteType;
        #Check if the move is en passant
        elif (referenceBoard[possibleMmT[i][0]] & pawnPrmChk == wPawnBf\
            and (abs(possibleMmT[i][1] - possibleMmT[i][0]) == 7 or abs(possibleMmT[i][1] - possibleMmT[i][0]) == 9)\
            and referenceBoard[possibleMmT[i][1]] == 0):
            tempBoard = list(referenceBoard);
            tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]];
            tempBoard[possibleMmT[i][0]] = whiteType;
            tempBoard[Rank2FdPawnSqr] = whiteType;
            print("Simulate en passant:", possibleMmT[i][0], possibleMmT[i][1]);
        #Other moves
        else:
            InnerR2FdPawnSqr = None;
            if (referenceBoard[possibleMmT[i][0]] & pawnPrmChk == wPawnBf and abs(possibleMmT[i][1] - possibleMmT[i][0]) == 16):
                InnerR2FdPawnSqr = possibleMmT[i][1];
                
            tempBoard = list(referenceBoard);
            tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]];
            tempBoard[possibleMmT[i][0]] = whiteType;
        #refreshBoard(pvcPColorBf, tempBoard, 0);#Delete the head # to visualize simulation

        if(turnsSimulated == turnsToSimulate or (turnsNum == 1 and pvcCColorBf == whiteType) or checkMateTest == 1):
            tempMoveValue[i] = moveValueCalculation(tempBoard, currentColorBf, turnsSimulated);#Calculate moveValue

        #When computer starts the game first, skip simulations for the next turn
        if(turnsSimulated < turnsToSimulate and ((turnsNum == 1 and pvcCColorBf == whiteType) != 1) and checkMateTest != 1):
            if (route == -1):
                aiMoveDecide(tempBoard, turnsSimulated, i, turnColor, 0, infoList, InnerR2FdPawnSqr);
            else:
                aiMoveDecide(tempBoard, turnsSimulated, route, turnColor, 0, infoList, InnerR2FdPawnSqr);


    if (checkMateTest == 1):
        #print("checkMateTest value list:", tempMoveValue);
        return max(tempMoveValue);
    #When computer starts the game first, skip the rest simulations and do some random moves
    elif (turnsNum == 1 and pvcCColorBf == whiteType):
        randMaxValue = random.randint(1, 3);
        while (randMaxValue > 1):
            tempMoveValue[tempMoveValue.index(max(tempMoveValue))] = 0;
            randMaxValue -= 1;
        lastMoveValueL[tempMoveValue.index(max(tempMoveValue))] = (max(tempMoveValue));
        return;
    
    if(turnsSimulated < turnsToSimulate):
        if (moveAdvantageL[route][turnsSimulated] == len(possibleMmT)):
            moveAdvantageL[route][turnsSimulated - 1] += 1;
            moveAdvantageL[route][turnsSimulated] = 1;
            
    elif(turnsSimulated == turnsToSimulate):
        if (turnsToSimulate != 1):
            if (max(tempMoveValue) > initBoardValue or abs((0.00001 + max(tempMoveValue) - initBoardValue) / (0.00001 + max(tempMoveValue))) < 0.01001):
                moveAdvantageL[route][turnsSimulated - 1] += 1;
            #Assume the previous play is the best move for last turn to have the minimum move value
            if (max(tempMoveValue) < lastMoveValueL[route]):
                lastMoveValueL[route] = max(tempMoveValue);

                #if (turnsNum == 3):
                    #tempBoard = list(referenceBoard);
                    #tempBoard[possibleMmT[tempMoveValue.index(max(tempMoveValue))][1]] = tempBoard[possibleMmT[tempMoveValue.index(max(tempMoveValue))][0]];
                    #tempBoard[possibleMmT[tempMoveValue.index(max(tempMoveValue))][0]] = whiteType;
                    #refreshBoard(0, tempBoard, 0)
                    #print(route);
                    #input(max(tempMoveValue));
        else:
            lastMoveValueL[tempMoveValue.index(max(tempMoveValue))] = (max(tempMoveValue));
                
 
#Start Turn, usually declare lastly
def nextTurn(turnsNum):
    global board;
    global gameOver;
    global hiddenTerritory;
    global wLRookMoved;
    global wRRookMoved;
    global bLRookMoved;
    global bRRookMoved;
    global wKingMoved;
    global bKingMoved;
    global Rank2FdPawnSqr;
    
    print("Turn:");
    if (turnsNum % 2 == 1):
        turnColor = whiteType;
        print("White");
        oppTurnColor = blackType;
    else:
        turnColor = blackType;
        print("Black");
        oppTurnColor = whiteType;
        
    if (gameMode == 1 and turnsNum > 1):#Board is already initialized and drawn at turnsNum = 1
        ttScreen.ontimer(None, 1000);
        refreshBoard(turnColor == blackType, board, 1);

    possibleMmT = movementTrack(board, turnColor, moveInfoList(), Rank2FdPawnSqr);#All moves avilable in the lists of (startSqr, endSqr)
    
    moveCommandSucc = 0;
    while(moveCommandSucc == 0):
        #Player inputs at player's turn
        if((gameMode == 1) or (gameMode == 2 and turnColor == pvcPColorBf)):
            moveCommand = input("Command your piece in the example format of \"a1a2\", \"a12\" or \"ab1\".")
            #Check a1b1 type
            if ((len(moveCommand) == 4)\
                and moveCommand[0].isdigit() == 0 and moveCommand[1].isdigit()\
                and moveCommand[2].isdigit() == 0 and moveCommand[3].isdigit()):
                startPointX = int(transformCharCoord(moveCommand[0]));
                startPointY = int(moveCommand[1]);
                endPointX = int(transformCharCoord(moveCommand[2]));
                endPointY = int(moveCommand[3]);
            #Check a12 type
            elif ((len(moveCommand) == 3)\
                and moveCommand[0].isdigit() == 0 and moveCommand[1].isdigit() and moveCommand[2].isdigit()):
                startPointX = int(transformCharCoord(moveCommand[0]));
                startPointY = int(moveCommand[1]);
                endPointX = int(transformCharCoord(moveCommand[0]));
                endPointY = int(moveCommand[2]);
            #Check ab1 type
            elif ((len(moveCommand) == 3)\
                and moveCommand[0].isdigit() == 0 and moveCommand[1].isdigit() == 0 and moveCommand[2].isdigit()):
                startPointX = int(transformCharCoord(moveCommand[0]));
                startPointY = int(moveCommand[2]);
                endPointX = int(transformCharCoord(moveCommand[1]));
                endPointY = int(moveCommand[2]);
            else:
                startPointX = -1;
                startPointY = -1;
                endPointX = -1;
                endPointY = -1;
        #AI inputs at AI's turn     
        elif(gameMode == 2 and turnColor != pvcPColorBf):
            aiMoveDecide(board, 0, -1, turnColor, 0, moveInfoList(), Rank2FdPawnSqr);
            #print("moveAdvantageL", moveAdvantageL);
            #print("lastMoveValueL", lastMoveValueL);
                        
            moveValueL = [];
            createNestedLists(moveValueL, len(possibleMmT));
            for x in range(len(possibleMmT)):
                if (moveAdvantageL[x] == max(moveAdvantageL)):
                    moveValueL[x].append(1);
                else:
                    moveValueL[x].append(0);
                if(turnsToSimulate % 2 == 1):
                    moveValueL[x].append(lastMoveValueL[x]);

            #print(moveValueL);
            #print(max(moveValueL));
            #print(possibleMmT);
            aiDecideStSqr = possibleMmT[moveValueL.index(max(moveValueL))][0];
            aiDecideEndSqr = possibleMmT[moveValueL.index(max(moveValueL))][1];
            #print(aiDecideStSqr, aiDecideEndSqr);
            #input("wait");
            startPointX = (aiDecideStSqr % 8) + 1;
            startPointY = int(aiDecideStSqr / 8) + 1;
            endPointX = (aiDecideEndSqr % 8) + 1;
            endPointY = int(aiDecideEndSqr / 8) + 1;
        #print(startPointX, startPointY, endPointX, endPointY);
    
        if (1 <= startPointX <= 8 and 1 <= startPointY <= 8 and 1 <= endPointX <= 8 and 1 <= endPointY <= 8):
            startSqr = (startPointX - 1) + ((startPointY - 1) * 8);
            endSqr = (endPointX - 1) + ((endPointY - 1) * 8);
            #inverse coord at player black's turn
            if((gameMode == 1 and turnColor == blackType) or (gameMode == 2 and turnColor == blackType and pvcPColorBf == blackType)):
                startSqr = 63 - startSqr;
                endSqr = 63 - endSqr;
            #print(startSqr, endSqr);
            if(board[startSqr] > 0):
                if(board[startSqr] & blackType == turnColor):
                    outOfRange = 1;
                    for i in range(len(possibleMmT)):
                        if (possibleMmT[i][0] == startSqr and possibleMmT[i][1] == endSqr):
                            outOfRange = 0;
                            tempBoard = list(board);
                            #Check if the move is castling
                            if (startSqr == 4 and endSqr == 2\
                                and tempBoard[4] & bKingBf == wKingBf and tempBoard[0] & bLRookBf == wLRookBf):
                                wLRookMoved = 1;
                                wKingMoved = 1;
                                tempBoard[4] = whiteType;
                                tempBoard[0] = whiteType;
                                tempBoard[2] = wKingBf;
                                tempBoard[3] = wLRookBf;
                            elif (startSqr == 60 and endSqr == 58\
                                and tempBoard[60] & bKingBf == bKingBf and tempBoard[56] & bLRookBf == bRookBf):
                                bLRookMoved = 1;
                                bKingMoved = 1;
                                tempBoard[60] = whiteType;
                                tempBoard[56] = whiteType;
                                tempBoard[58] = bKingBf;
                                tempBoard[59] = bRookBf;
                            elif (startSqr == 4 and endSqr == 6\
                                and tempBoard[4] & bKingBf == wKingBf and tempBoard[7] & bLRookBf == wRookBf):
                                wRRookMoved = 1;
                                wKingMoved = 1;
                                tempBoard[4] = whiteType;
                                tempBoard[7] = whiteType;
                                tempBoard[6] = wKingBf;
                                tempBoard[5] = wRookBf;
                            elif (startSqr == 60 and endSqr == 62\
                                and tempBoard[60] & bKingBf == bKingBf and tempBoard[63] & bLRookBf == bLRookBf):
                                bRRookMoved = 1;
                                bKingMoved = 1;
                                tempBoard[60] = whiteType;
                                tempBoard[63] = whiteType;
                                tempBoard[62] = bKingBf;
                                tempBoard[61] = bLRookBf;
                            #Check if the move is promotion
                            elif (len(possibleMmT[i]) == 3 and tempBoard[possibleMmT[i][0]] & pawnPrmChk == wPawnBf):
                                promoteToPiece = None;
                                if (gameMode == 1):
                                    while (1):
                                        promoteToPiece = input("Enter \"q\", \"k\", \"r\" or \"b\" to promote your pawn to a queen, knight, rook or bishop.");
                                        if (promoteToPiece == "q" or promoteToPiece == "k" or promoteToPiece == "r" or promoteToPiece == "b"):
                                            break;   
                                if (((gameMode == 1 or (gameMode == 2 and turnColor == pvcPColorBf)) and promoteToPiece == "q")\
                                    or (gameMode == 2 and turnColor == pvcCColorBf and possibleMmT[i][2] == 0)):
                                    tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wQueenBf;
                                    tempBoard[possibleMmT[i][0]] = whiteType;
                                if (((gameMode == 1 or (gameMode == 2 and turnColor == pvcPColorBf)) and promoteToPiece == "k")\
                                    or (gameMode == 2 and turnColor == pvcCColorBf and possibleMmT[i][2] == 1)):
                                    tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wKnightBf;
                                    tempBoard[possibleMmT[i][0]] = whiteType;
                                if (((gameMode == 1 or (gameMode == 2 and turnColor == pvcPColorBf)) and promoteToPiece == "r")\
                                    or (gameMode == 2 and turnColor == pvcCColorBf and possibleMmT[i][2] == 2)):
                                    tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wRookBf;
                                    tempBoard[possibleMmT[i][0]] = whiteType;
                                if (((gameMode == 1 or (gameMode == 2 and turnColor == pvcPColorBf)) and promoteToPiece == "b")\
                                    or (gameMode == 2 and turnColor == pvcCColorBf and possibleMmT[i][2] == 3)):
                                    tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]] | wBishopBf;
                                    tempBoard[possibleMmT[i][0]] = whiteType;
                            #Check if the move is en passant
                            elif (tempBoard[possibleMmT[i][0]] & pawnPrmChk == wPawnBf\
                                and (abs(possibleMmT[i][1] - possibleMmT[i][0]) == 7 or abs(possibleMmT[i][1] - possibleMmT[i][0]) == 9)\
                                and tempBoard[possibleMmT[i][1]] == 0):
                                tempBoard[possibleMmT[i][1]] = tempBoard[possibleMmT[i][0]];
                                tempBoard[possibleMmT[i][0]] = whiteType;
                                tempBoard[Rank2FdPawnSqr] = whiteType;
                            #Other moves
                            else:
                                tempBoard[endSqr] = tempBoard[startSqr];
                                tempBoard[startSqr] = whiteType;

                            #Check for suicide move
                            if ((aiMoveDecide(tempBoard, 0, -1, oppTurnColor, 1, moveInfoList(), Rank2FdPawnSqr) - baseValue) / -baseValue > 1.95):
                                print("You cannot leave your own king in checked! Try again.");
                                continue;
                            else:
                                Rank2FdPawnSqr = None;
                                
                                if (board[startSqr] & bLRookBf == wLRookBf and board[startSqr] & wPawnBf != wPawnBf):
                                    wLRookMoved = 1;
                                elif (board[startSqr] & bLRookBf == wRookBf and board[startSqr] & wPawnBf != wPawnBf):
                                    wRRookMoved = 1;
                                elif (board[startSqr] & bLRookBf == bLRookBf and board[startSqr] & wPawnBf != wPawnBf):
                                    bLRookMoved = 1;
                                elif (board[startSqr] & bLRookBf == bRookBf and board[startSqr] & wPawnBf != wPawnBf):
                                    bRRookMoved = 1;
                                if (board[startSqr] & bKingBf == wKingBf and board[startSqr] & wPawnBf != wPawnBf):
                                    wKingMoved = 1;
                                if (board[startSqr] & bKingBf == bKingBf and board[startSqr] & wPawnBf != wPawnBf):
                                    bKingMoved = 1;
                                if (board[startSqr] & pawnPrmChk == wPawnBf and abs(endSqr - startSqr) == 16):
                                    Rank2FdPawnSqr = endSqr;
                                    #print(Rank2FdPawnSqr);
                                    
                                board = list(tempBoard);
                                
                            #Check for checkmate move    
                            if ((aiMoveDecide(board, 0, -1, oppTurnColor, 1, moveInfoList(), Rank2FdPawnSqr) - baseValue) / -baseValue < 0.05):
                                gameOver = 1;#Set global at the top of the function

                            if (gameMode == 1):                              
                                refreshBoard(turnColor == blackType, board, 0);
                            elif (gameMode == 2):
                                refreshBoard(pvcPColorBf == blackType, board, 0);
                            
                            #Gameover
                            if(gameOver):
                                if(gameMode == 2):
                                    if(turnColor == pvcPColor):
                                        print("You win!");
                                    else:
                                        print("You lose.");
                                if(gameMode == 1):
                                    if(turnColor == whiteType):
                                        print("White wins!");
                                    else:
                                        print("Black wins!");
                                while(1):
                                    answer = input("Do you wish to play again?(enter \"y\"/\"n\")");
                                    if (answer == "y"):
                                        #Leave initial turtle
                                        for x in range(1, len(ttL) - 1):
                                            del ttL[1];
                                            ttL.remove(ttL[1]);
                                        return -1;
                                    if (answer == "n"):
                                        turtle.bye();
                                        quit();
                        
                            turnsNum += 1;
                            moveCommandSucc = 1;
                            return turnsNum;
                                    
                    if (outOfRange == 1):   
                        print("The destined square has outreached the piece's moving range! Try again.");
                else:
                    print("You cannot move the opposite color! Try again.");
            else:
                print("There has no piece on the chosen square! Try again.");
        else:
            print("Invalid command");


while(1):
    #_main
    turtle.reset();
    turtle.title("Pixel Chess");
    screenWidth = 350;
    screenHeight = 350;
    turtle.setup(screenWidth * 1.1, screenHeight * 1.1, -1, 1);
    turtle.bgpic("Ground_cherry_blossom.gif");
    ttScreen = turtle.getscreen();
    ttScreen.addshape("Loading_icon.gif");
    turtle.shape("Loading_icon.gif");
    ttScreen.screensize(screenWidth, screenHeight);
    boardWidth = 295;
    boardHeight = 225;
    widthSqrSize = boardWidth / 8;
    heightSqrSize = boardHeight / 8;
    darkSqrColor = "#6d6dc4";#"#236e61";
    lightSqrColor = "#e5f698";
    fontColor = "#362e25";
    keyInput = None;

    turtle0 = turtle.Turtle();#Pen
    turtle1 = turtle.Turtle();#Board
    turtle2 = turtle.Turtle();#wKing
    turtle3 = turtle.Turtle();#wR1Pawn
    turtle4 = turtle.Turtle();#wR2Pawn
    turtle5 = turtle.Turtle();#wR3Pawn
    turtle6 = turtle.Turtle();#wR4Pawn
    turtle7 = turtle.Turtle();#wL4Pawn
    turtle8 = turtle.Turtle();#wL3Pawn
    turtle9 = turtle.Turtle();#wL2Pawn
    turtle10 = turtle.Turtle();#wL1Pawn
    turtle11 = turtle.Turtle();#wQueen
    turtle12 = turtle.Turtle();#wRBishop
    turtle13 = turtle.Turtle();#wLBishop
    turtle14 = turtle.Turtle();#wRKnight
    turtle15 = turtle.Turtle();#wLKnight
    turtle16 = turtle.Turtle();#wRRook
    turtle17 = turtle.Turtle();#wLRook
    turtle18 = turtle.Turtle();#bKing
    turtle19 = turtle.Turtle();#bR1Pawn
    turtle20 = turtle.Turtle();#bR2Pawn
    turtle21 = turtle.Turtle();#bR3Pawn
    turtle22 = turtle.Turtle();#bR4Pawn
    turtle23 = turtle.Turtle();#bL4Pawn
    turtle24 = turtle.Turtle();#bL3Pawn
    turtle25 = turtle.Turtle();#bL2Pawn
    turtle26 = turtle.Turtle();#bL1Pawn
    turtle27 = turtle.Turtle();#bQueen
    turtle28 = turtle.Turtle();#bRBishop
    turtle29 = turtle.Turtle();#bLBishop
    turtle30 = turtle.Turtle();#bRKnight
    turtle31 = turtle.Turtle();#bLKnight
    turtle32 = turtle.Turtle();#bRRook
    turtle33 = turtle.Turtle();#bLRook
    
    #Initial turtle should be at position 0
    ttL = [turtle, turtle0, turtle1, turtle2, turtle3, turtle4, turtle5, turtle6, turtle7, turtle8,\
           turtle9, turtle10, turtle11, turtle12, turtle13, turtle14, turtle15, turtle16, turtle17, turtle18,\
           turtle19, turtle20, turtle21, turtle22, turtle23, turtle24, turtle25, turtle26, turtle27, turtle28,\
           turtle29, turtle30, turtle31, turtle32, turtle33];

    for x in range(1, len(ttL)):
        ttL[x].hideturtle();
        ttL[x].speed(1);
        ttL[x].up();

    turtle.hideturtle();
    turtle.tracer(0,0);#Default to no update
    turtle0.speed(0);
    turtle0.color(fontColor, darkSqrColor);
    turtle1.showturtle();
    turtle.up();
    
    boardImage = "Chess_Atrb_N//chess_board_2.gif"
    ttScreen.addshape(boardImage);
    turtle1.goto(1, -8);

    turtle1.shape(boardImage);
    for x in range(0,64):
        goEraseSqr(x);
    
    wKingImage = "Chess_Atrb_N//chess_piece_white_king_2.gif"
    ttScreen.addshape(wKingImage);
    wPawnImage = "Chess_Atrb_N//chess_piece_white_pawn_2.gif"
    ttScreen.addshape(wPawnImage);
    wQueenImage = "Chess_Atrb_N//chess_piece_white_queen_2.gif"
    ttScreen.addshape(wQueenImage);
    wBishopImage = "Chess_Atrb_N//chess_piece_white_bishop_2.gif"
    ttScreen.addshape(wBishopImage);
    wKnightImage = "Chess_Atrb_N//chess_piece_white_knight_2.gif"
    ttScreen.addshape(wKnightImage);
    wRookImage = "Chess_Atrb_N//chess_piece_white_rook.gif"
    ttScreen.addshape(wRookImage);
    bKingImage = "Chess_Atrb_N//chess_piece_black_king_2.gif"
    ttScreen.addshape(bKingImage);
    bPawnImage = "Chess_Atrb_N//chess_piece_black_pawn_2.gif"
    ttScreen.addshape(bPawnImage);
    bQueenImage = "Chess_Atrb_N//chess_piece_black_queen_2.gif"
    ttScreen.addshape(bQueenImage);
    bBishopImage = "Chess_Atrb_N//chess_piece_black_bishop_2.gif"
    ttScreen.addshape(bBishopImage);
    bKnightImage = "Chess_Atrb_N//chess_piece_black_knight_2.gif"
    ttScreen.addshape(bKnightImage);
    bRookImage = "Chess_Atrb_N//chess_piece_black_rook.gif"
    ttScreen.addshape(bRookImage);

    turtle2.shape(wKingImage);
    turtle3.shape(wPawnImage);
    turtle4.shape(wPawnImage);
    turtle5.shape(wPawnImage);
    turtle6.shape(wPawnImage);
    turtle7.shape(wPawnImage);
    turtle8.shape(wPawnImage);
    turtle9.shape(wPawnImage);
    turtle10.shape(wPawnImage);
    turtle11.shape(wQueenImage);
    turtle12.shape(wBishopImage);
    turtle13.shape(wBishopImage);
    turtle14.shape(wKnightImage);
    turtle15.shape(wKnightImage);
    turtle16.shape(wRookImage);
    turtle17.shape(wRookImage);
    turtle18.shape(bKingImage);
    turtle19.shape(bPawnImage);
    turtle20.shape(bPawnImage);
    turtle21.shape(bPawnImage);
    turtle22.shape(bPawnImage);
    turtle23.shape(bPawnImage);
    turtle24.shape(bPawnImage);
    turtle25.shape(bPawnImage);
    turtle26.shape(bPawnImage);
    turtle27.shape(bQueenImage);
    turtle28.shape(bBishopImage);
    turtle29.shape(bBishopImage);
    turtle30.shape(bKnightImage);
    turtle31.shape(bKnightImage);
    turtle32.shape(bRookImage);
    turtle33.shape(bRookImage);
    
    ttWL = [turtle2, turtle3, turtle4, turtle5, turtle6, turtle7, turtle8, turtle9,\
            turtle10, turtle11, turtle12, turtle13, turtle14, turtle15, turtle16, turtle17];
    ttBL = [turtle18, turtle19, turtle20, turtle21, turtle22, turtle23, turtle24, turtle25,\
            turtle26, turtle27, turtle28, turtle29, turtle30, turtle31, turtle32, turtle33];

    #(wKStampId, wR1PStampId, wR2PStampId, wR3PStampId, wR4PStampId, wL4PStampId, wL3PStampId, wL2PStampId,
    # wL1PStampId, wQStampId, wRBStampId, wLBStampId, wRNStampId, wLNStampId, wRRStampId, wLRStampId)
    #Black list is similar to above
    ttWStampIdL = [None] * 16;
    ttBStampIdL = [None] * 16;
    #lists similar to above
    capturedwL = [0] * 16;
    capturedbL = [0] * 16;

    Rank2FdPawnSqr = None;
    
    #Set bitflag for piece type
    whiteType   = 0b0000000000;#Should always be zero
    blackType   = 0b0001000000;

    pawnPrmChk  = 0b0000011111;
    
    wBishopBf   = 0b0000000010;
    wKnightBf   = 0b0000000100;
    wRookBf     = 0b0000001000;
    wQueenBf    = 0b0000010000;
    wKingBf     = 0b0000100000;
    wLBishopBf  = 0b0010000010;
    wLKnightBf  = 0b0010000100;
    wLRookBf    = 0b0010001000;
    
    wPawnBf     = 0b0000000001;#May not refer to pawn type when used with "&" due to promotion
    wR2PawnBf   = 0b0100000001;
    wR3PawnBf   = 0b1000000001;
    wR4PawnBf   = 0b1100000001;
    wLPawnBf    = 0b0010000001;
    wL2PawnBf   = 0b0110000001;
    wL3PawnBf   = 0b1010000001;
    wL4PawnBf   = 0b1110000001;
    
    bBishopBf   = 0b0001000010;
    bKnightBf   = 0b0001000100;
    bRookBf     = 0b0001001000;
    bQueenBf    = 0b0001010000;
    bKingBf     = 0b0001100000;
    bLBishopBf  = 0b0011000010;
    bLKnightBf  = 0b0011000100;
    bLRookBf    = 0b0011001000;

    bPawnBf     = 0b0001000001;
    bR2PawnBf   = 0b0101000001;
    bR3PawnBf   = 0b1001000001;
    bR4PawnBf   = 0b1101000001;
    bLPawnBf    = 0b0011000001;
    bL2PawnBf   = 0b0111000001;
    bL3PawnBf   = 0b1011000001;
    bL4PawnBf   = 0b1111000001;
    
    
    board = [];
    turnsNum = 0;
    previousTurnsNum = 0;
    baseValue = -9999;#Move value equivalent to losing
    gameOver = 0;
    iMTAllyInRange = [];
    createNestedLists(iMTAllyInRange, 64);
    hiddenTerritory = [];#Set global at top of the function
    createNestedLists(hiddenTerritory, 64);
    #bool for below var, only 1 and 0 are allowed
    wLRookMoved = 0;
    wRRookMoved = 0;
    bLRookMoved = 0;
    bRRookMoved = 0;
    wKingMoved = 0;
    bKingMoved = 0;
    
    #Set bitflag for square condition(black territory, white territory)
    zeroCdt = 0b00;
    wTerritory = 0b01;
    bTerritory = 0b10;
    mixedTerritory = 0b11;
    #Set board
    for x in range(0,64):
        board.append(whiteType);#whiteType here refers zero
    
    #Place pieces on board,
    #with sequence
        #"two digit, unit digit(the specific piece counting from the 1-4th position on each side),
        #, side(0 = left and 1 = right piece of the same type for castling), color(0 = white, 1 = black)
        #, king, queen, rook, knight, bishop, pawn"
    #Should be set as the only place where the pieces are added.
    board[0] = wLRookBf;
    board[1] = wLKnightBf;
    board[2] = wLBishopBf;
    board[3] = wQueenBf;
    board[4] = wKingBf;
    board[5] = wBishopBf;
    board[6] = wKnightBf;
    board[7] = wRookBf;
    board[8] = wLPawnBf;
    board[9] = wL2PawnBf;
    board[10] = wL3PawnBf;
    board[11] = wL4PawnBf;
    board[12] = wR4PawnBf;
    board[13] = wR3PawnBf;
    board[14] = wR2PawnBf;
    board[15] = wPawnBf;
    board[56] = bRookBf;
    board[57] = bKnightBf;
    board[58] = bBishopBf;
    board[59] = bQueenBf;
    board[60] = bKingBf;
    board[61] = bLBishopBf;
    board[62] = bLKnightBf;
    board[63] = bLRookBf;
    board[48] = bPawnBf;
    board[49] = bR2PawnBf;
    board[50] = bR3PawnBf;
    board[51] = bR4PawnBf;
    board[52] = bL4PawnBf;
    board[53] = bL3PawnBf;
    board[54] = bL2PawnBf;
    board[55] = bLPawnBf;

    #Test
    #testBoard = [0]*64;
    #testBoard[0] = wLRookBf;
    #testBoard[4] = bRookBf;
    #print(moveValueCalculation(testBoard, whiteType, whiteType, 1));
    
    #Start Game
    while(1):
        gameMode = int(input("Choose a game mode. Enter \"1\" for PvP or enter \"2\" for PvC."));
        if (gameMode == 1 or gameMode == 2):
            break;
        else:
            print("You can only choose between 1 or 2. Try again!");
            
    if (gameMode == 1):
        turnsToSimulate = 1;
        
    if (gameMode == 2):
        while(1):
            pvcPColor = int(input("Choose your color. Enter \"1\" for white or enter \"2\" for black."));
            if (pvcPColor == 1 or pvcPColor == 2):
                break;
            else:
                print("You can only choose between 1 or 2. Try again!");
        #Set the color for computer in bitflags
        if (pvcPColor == 1):
            pvcCColorBf = blackType;
            pvcPColorBf = whiteType;
        else:
            pvcCColorBf = whiteType;
            pvcPColorBf = blackType;
        while(1):
            turnsToSimulate = int(input("Enter an odd number of turns the AI simulates when deciding a move."));
            if (turnsToSimulate % 2 == 1):
                break;
            else:
                print("You can only choose an odd number. Try again!");
    
    #Set pieces
    if (gameMode == 2 and pvcPColorBf == blackType):
        refreshBoard(1, board, 1);
    else:
        refreshBoard(0, board, 1);
    
    turnsNum += 1;
    while (turnsNum  > previousTurnsNum):
        previousTurnsNum = turnsNum;
        turnsNum = nextTurn(turnsNum);

turtle.done();
