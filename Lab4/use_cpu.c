//
//  jfs9, 10/18/16  v2, add variable for altering frequency
//                  v3 add internal timer
//                  v4 delayMicroseconds and Pinvalue for better behavior...
//        3/24/17   v6 nanosleep....
//        10/15/18     include stdlib

#include <stdio.h>
#include <stdlib.h>

int main (int argc, char** argv)
{
	float x = .00000001;
	float y = 1.0000001;
	for(int w =0; w <100000000; w++){
		for(int i =0; i < 10000000; i++){
			for(int j = 0; j <1000000; j++){
				y = (y + x/y)*y/y*y/y;
			}
		}
	}
}
