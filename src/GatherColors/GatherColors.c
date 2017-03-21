#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "GatherColors.h"

int GatherColors(char* buffer)
{
	char *currentWorkingDirectory;
	char bufferCWD[1024];

	currentWorkingDirectory = getcwd( bufferCWD, 1023 );

	char *script = "/src/GatherColors/GatherColorsPy.py";

	char *command;
	asprintf(&command, "python3 %s%s", currentWorkingDirectory, script);

	FILE *fd;

	if (( fd = popen(command, "r")) == NULL ) {
		printf("Error opening pipe!\n");
		return 1;
	}

	while (fgets(buffer, 128, fd) != NULL ) {
	}

	if ( pclose(fd) ) {
		printf( "Command not found or exited with error status\n");
		return 2;
	}

	return 0;
}
