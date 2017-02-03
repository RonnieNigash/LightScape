#include <stdio.h>
#include "GatherColors.h"

int GatherColors() {
	char *command = "python GatherColorsPy.py";

	char buffer[128];
	FILE *fd;

	if (( fd = popen(command, "r")) == NULL ) {
		printf("Error opening pipe!\n");
		return -1;
	}

	while (fgets(buffer, 128, fd) != NULL ) {
		printf("Output:\t%s", buffer);
	}

	if ( pclose(fd) ) {
		printf( "Command not found or exited with error status\n");
		return -1;
	}

	return 0;
}
