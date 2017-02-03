#include <stdlib.h>
#include "CppUTest/TestHarness.h"

extern "C" {
#include "GatherColors.h"
}


TEST_GROUP(GatherColors)
{
	char buffer[128];
	void setup()
	{
	}

	void teardown()
	{
	}

};

TEST(GatherColors, RunsGatherColorsScript)
{
	int returnVal = GatherColors(buffer);
	BYTES_EQUAL(0, returnVal);
}

TEST(GatherColors, FillsBuffer)
{
	int returnVal = GatherColors(buffer);
	BYTES_EQUAL(0, returnVal);
	CHECK_FALSE(buffer == NULL);
	printf("%s\n", buffer);
}
