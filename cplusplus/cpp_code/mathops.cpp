/*
 * mathops.cpp
 * 
 * Copyright 2026 Chris McHarg <cradlesinger@icloud.com>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <cmath>

int main(int argc, char **argv)
{
	
	double x = 1.0, y=2.0, z, s;
	z = x/y;		// division
	std::cout << "division: " << x << " / " << y << " = " << z << "\n";
	z = sqrt(x);	// square root
	std::cout << "square root of " << x << " = " << z << "\n";
	z = exp(y);		// Natural exponential function
	std::cout << "exponentiation of " << y << " = " << z << "\n";
	s = pow(x,y);	// x to the power of y
	std::cout << x << " to the power of " << y << " = " << z << "\n";
	z = M_PI;		// z stores the value of pi
	std::cout << "The value of Pi is " << z << "\n";
	
	// Declare an array
	int array1[2];
	double array2[3][3];
	
	// Initialise the arrays
	array1[0] = 1;
	array1[1] = 2;
	
	array2[0][0] = 6.4;
	array2[0][1] = -3.1;
	array2[0][2] = 55.0;
	array2[1][0] = 63.0;
	array2[1][1] = -100.9;
	array2[1][2] = 50.8;
	array2[2][0] = 13.2;
	array2[2][1] = 15.8;
	array2[2][2] = 11.2;
	
	std::cout << "/ " << array2[0][0] << " " << array2[0][1] << " " << array2[0][2] << " \\" << "\n";
	std::cout << "| " << array2[1][0] << " " << array2[1][1] << " " << array2[1][2] << " |" << "\n";
	std::cout << "\\ " << array2[2][0] << " " << array2[2][1] << " " << array2[2][2] << " /" << "\n";
	
	return 0;
}

