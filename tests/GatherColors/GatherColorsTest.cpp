#include <stdlib.h>
#include "CppUTest/TestHarness.h"

extern "C" {
#include "GatherColors.h"
}


TEST_GROUP(GatherColors)
{
	void setup()
	{
	}

	void teardown()
	{
	}

};

TEST(GatherColors, RunsGatherColorsScript)
{
	int returnVal = GatherColors();
	BYTES_EQUAL(0, returnVal);
}
