#include "DriveLEDs.h"

static uint16_t * addressOfLEDs;

static uint16_t LEDState; // records state of LEDs

enum {
	ALL_LEDS_ON = ~0,
	ALL_LEDS_OFF = ~ALL_LEDS_ON,
	FIRST_LED = 1,
	LAST_LED = 50
};

static void writeToHardware(void)
{
	*addressOfLEDs = LEDState;
}

void DriveLEDs_Create(uint16_t * address)
{
	addressOfLEDs = address;
	LEDState = (uint16_t)ALL_LEDS_OFF;
	writeToHardware();
}

void DriveLEDs_Destroy()
{
}
