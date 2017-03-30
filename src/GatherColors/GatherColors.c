#include "GatherColors.h"

int GatherColors(char* buffer)
{
	system("python3 `pwd`/src/GatherColors/GatherColorsPy.py &");

	return 0;
}
