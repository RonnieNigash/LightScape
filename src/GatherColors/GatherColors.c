#include "GatherColors.h"
/*int GatherColors() {
	return system("/usr/bin/osascript GetPixelColor.applescript");
}*/
int main(int argc, char** argv){
	system("/usr/bin/osascript GetPixelColor.applescript");
	return 1;
}
