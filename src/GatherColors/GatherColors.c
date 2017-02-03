#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "GatherColors.h"

int GatherColors(char* buffer) {

	char *currentWorkingDirectory;
	char bufferCWD[1024];

	currentWorkingDirectory = getcwd( bufferCWD, 1024 );

	char *python = "python ";
	char *script = "/src/GatherColors/GatherColorsPy.py";

	char *argument = malloc( strlen(script) + strlen(currentWorkingDirectory) + 1 );
	strcpy(argument, currentWorkingDirectory);
	strcat(argument, script);

	char *command = malloc( strlen(python) + strlen(currentWorkingDirectory) + strlen(script) + 1 );
	strcpy(command, python);
	strcat(command, argument);


	FILE *fd;

	if (( fd = popen(command, "r")) == NULL ) {
		printf("Error opening pipe!\n");
		return -1;
	}

	while (fgets(buffer, 128, fd) != NULL ) {
	}

	if ( pclose(fd) ) {
		printf( "Command not found or exited with error status\n");
		return -1;
	}


	free(argument);
	free(command);

	return 0;
}
