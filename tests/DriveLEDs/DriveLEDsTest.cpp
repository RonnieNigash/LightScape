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

TEST(DriveLEDs, LastAndFirstLEDs)
{
	DriveLEDs_TurnOn(1);
	DriveLEDs_TurnOn(64);
	BYTES_EQUAL(0x8001, virtualLEDStrip);
}

TEST(DriveLEDs, QueryLEDStateOn)
{
	CHECK_FALSE(DriveLEDs_IsOn(3));
	DriveLEDs_TurnOn(6);
	CHECK_TRUE(DriveLEDs_IsOn(6));
}

TEST(DriveLEDs, OutOfBoundsNoChange)
{
	DriveLEDs_TurnOn(1000);
	BYTES_EQUAL(0, virtualLEDStrip);
}

TEST(DriveLEDs, QueryStateOutOfBounds)
{
	DriveLEDs_TurnAllOn();
	CHECK_FALSE(DriveLEDs_IsOn(65));
}

TEST(DriveLEDs, QueryLEDStateOff)
{
	DriveLEDs_TurnAllOn();
	DriveLEDs_TurnOff(6);
	CHECK_TRUE(DriveLEDs_IsOff(6));
}

TEST(DriveLEDs, TestAllColorsOff)
{
	LED firstLED = DriveLEDs_ReadColor(1);
	CHECK_TRUE(firstLED.green == 0);
	CHECK_TRUE(firstLED.red == 0);
	CHECK_TRUE(firstLED.blue == 0);
}

TEST(DriveLEDs, TestSetColors)
{
	DriveLEDs_SetColor(1, 255, 255, 255);
	LED firstLED = DriveLEDs_ReadColor(1);
	CHECK_TRUE(firstLED.green == 255);
	CHECK_TRUE(firstLED.red == 255);
	CHECK_TRUE(firstLED.blue == 255);
}

TEST(DriveLEDs, TestBoundaryColors)
{
	DriveLEDs_TurnAllOn();
	LED lastLED = DriveLEDs_ReadColor(63);
	CHECK_TRUE(lastLED.green == 255);
	CHECK_TRUE(lastLED.red == 255);
	CHECK_TRUE(lastLED.blue == 255);
}

