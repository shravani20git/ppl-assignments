airport(toronto,50,60).
airport(madrid,75,45).
airport(malaga,50,30).
airport(barcelona,40,30).
airport(valencia,40,20).
airport(london,75,80).
airport(paris,50,60).
airport(toulouse,40,30).
flight(toronto,air_canada,london,500,360).
flight(toronto,united,london,650,420).
flight(toronto,air_canada,madrid,900,480).
flight(toronto,united,madrid,950,540).
flight(toronto,iberia,madrid,800,480).
flight(madrid,iberia,malaga,50,60).
flight(madrid,iberia,valencia,40,50).
flight(madrid,iberia,barcelona,120,65).
flight(madrid,air_canada,barcelona,100,60).
flight(madrid,air_canada,toronto,900,480).
flight(madrid,united,toronto,950,540).
flight(madrid,iberia,toronto,800,480).
flight(valencia,iberia,malaga,80,120).
flight(valencia,iberia,madrid,40,50).
flight(valencia,iberia,barcelona,110,75).
flight(london,air_canada,toronto,500,360).
flight(london,united,toronto,650,420).
flight(london,iberia,220,240).
flight(barcelona,iberia,valencia,110,75).
flight(barcelona,iberia,madrid,120,65).
flight(barcelona,air_canada,100,60).
flight(malaga,iberia,valencia,80,120).
flight(malaga,iberia,madrid,50,60).
flight(paris,united,toulouse,35,120).
flight(toulouse,united,paris,35,120).

available(A,B):-flight(A,_,B,_,_).
cheap_flight(A,B,C):-flight(A,C,B,X,_),(X<400).
route_available(A,B):-flight(A,X,D,_,_),flight(D,Y,B,_,_).
preferrable(A,B,C):-flight(A,C,B,X,_),((X<400);(C = air_canada)).
united_and_air_canada(A,B):-(flight(A,X,B,_,_),(X=united)) -> (flight(A,Y,B,_,_),(Y=air_canada)).


