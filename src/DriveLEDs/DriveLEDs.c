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

static uint16_t convertLEDNumberToBit(uint16_t LEDNumber)
{
	return (uint16_t)(1 << (LEDNumber - 1));
}

static uint16_t LEDOutOfBounds(uint16_t LEDNumber)
{
	return (LEDNumber < FIRST_LED) || (LEDNumber > LAST_LED);
}

static void setLEDImageBit(uint16_t LEDNumber)
{
	LEDState |= convertLEDNumberToBit(LEDNumber);
}

void DriveLEDs_TurnOn(uint16_t LEDNumber)
{
	if (LEDOutOfBounds(LEDNumber)) {
		return;
	}

	setLEDImageBit(LEDNumber);
	writeToHardware();
}

static void clearLEDImageBit(uint16_t LEDNumber)
{
	LEDState &= ~(convertLEDNumberToBit(LEDNumber));
}

void DriveLEDs_TurnOff(uint16_t LEDNumber)
{
	if (LEDOutOfBounds(LEDNumber)) {
		return;
	}

	clearLEDImageBit(LEDNumber);
	writeToHardware();
}

