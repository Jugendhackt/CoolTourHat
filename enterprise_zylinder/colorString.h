#include "Hsv.h"
#define COLOR_MODE_SINGLE 1
#define COLOR_MODE_SINUS_RAINBOW 2
#define COLOR_MODE_HSV_RAINBOW 3
#define COLOR_MODE_TRICOLOR 4
#define COLOR_MODE_RANDOM 5

typedef struct _colorString {
	char const *string;
	int colorMode;
	rgb color;
	struct _colorString* next;

} colorString;