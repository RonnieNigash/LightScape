#ifndef D_DriveLEDs_H
#define D_DriveLEDs_H

void DriveLEDs_Create(uint16_t * address);
void DriveLEDs_Destroy(void);
void DriveLEDs_TurnOn(uint16_t LEDNumber);
void DriveLEDs_TurnOff(uint16_t LEDNumber);
void DriveLEDs_TurnAllOn(void);
bool DriveLEDs_IsOn(uint16_t LEDNumber);
bool DriveLEDs_IsOff(uint16_t LEDNumber);

#endif /* D_DriveLEDs_H */
