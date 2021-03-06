#include <stdbool.h>
#include "DriveLEDs.h"

static uint16_t * addressOfLEDs;

static uint16_t LEDState; // records state of LEDs

enum {
	ALL_LEDS_ON = ~0,
	ALL_LEDS_OFF = ~ALL_LEDS_ON,
	FIRST_LED = 1,
	LAST_LED = 64
};

static LED colors[LAST_LED];

static void writeToHardware(void)
{
	*addressOfLEDs = LEDState;
}

static void fillStrip(uint8_t g, uint8_t r, uint8_t b)
{
	uint16_t i;
	for (i = 0; i <= LAST_LED-FIRST_LED; i++) {
		DriveLEDs_SetColor(i, g, r, b);
	}
}

void DriveLEDs_Create(uint16_t * address)
{
	addressOfLEDs = address;
	LEDState = (uint16_t)ALL_LEDS_OFF;
	fillStrip(0, 0, 0);
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

void DriveLEDs_TurnAllOn(void)
{
	LEDState = (uint16_t)ALL_LEDS_ON;
	fillStrip(255, 255, 255);
	writeToHardware();
}


bool DriveLEDs_IsOn(uint16_t LEDNumber)
{
	if (LEDOutOfBounds(LEDNumber)) {
		return false;
	}

	return LEDState & convertLEDNumberToBit(LEDNumber);
}

bool DriveLEDs_IsOff(uint16_t LEDNumber)
{
	return !DriveLEDs_IsOn(LEDNumber);
}

void DriveLEDs_SetColor(uint16_t LEDNumber, uint8_t g, uint8_t r, uint8_t b)
{
	if (LEDOutOfBounds(LEDNumber)) {
		return;
	}

	colors[LEDNumber].green = g;
	colors[LEDNumber].red = r;
	colors[LEDNumber].blue = b;
}

// assumes LEDNumber is in bounds
LED DriveLEDs_ReadColor(uint16_t LEDNumber)
{
	return colors[LEDNumber];
}
