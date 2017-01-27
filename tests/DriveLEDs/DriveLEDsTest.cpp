#include <stdlib.h>
#include "CppUTest/TestHarness.h"

extern "C" {
#include "DriveLEDs.h"
}

/* ** Test List **
 * All LEDs turned off on initialization
 * Single LED turned on
 * Single LED turned off
 * Multiple LEDs turned on/off
 * Turn on all LEDs
 * Turn off all LEDs
 * Query LED state
 * Give LED color
 * **
*/

TEST_GROUP(DriveLEDs)
{
	uint16_t virtualLEDStrip;
	void setup()
	{
		DriveLEDs_Create(&virtualLEDStrip);
	}

	void teardown()
	{
		DriveLEDs_Destroy();
	}

};

TEST(DriveLEDs, LEDsOffAfterInitialization)
{
	virtualLEDStrip = 0xffff;
	DriveLEDs_Create(&virtualLEDStrip);
	BYTES_EQUAL(0, virtualLEDStrip);
}

TEST(DriveLEDs, TurnOnSingleLED)
{
	DriveLEDs_TurnOn(1);
	BYTES_EQUAL(1, virtualLEDStrip);
}

TEST(DriveLEDs, TurnOffSingleLED)
{
	DriveLEDs_TurnOn(1);
	DriveLEDs_TurnOff(1);
	BYTES_EQUAL(0, virtualLEDStrip);
}

TEST(DriveLEDs, MultipleLEDsOnOff)
{
	DriveLEDs_TurnAllOn();
	DriveLEDs_TurnOff(2);
	BYTES_EQUAL(0xfffd, virtualLEDStrip);
}


