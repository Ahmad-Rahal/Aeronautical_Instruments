################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/vl6180x/vl6180x_api.c \
../src/vl6180x/vl6180x_lib.c \
../src/vl6180x/x-nucleo-6180xa1.c 

OBJS += \
./src/vl6180x/vl6180x_api.o \
./src/vl6180x/vl6180x_lib.o \
./src/vl6180x/x-nucleo-6180xa1.o 

C_DEPS += \
./src/vl6180x/vl6180x_api.d \
./src/vl6180x/vl6180x_lib.d \
./src/vl6180x/x-nucleo-6180xa1.d 


# Each subdirectory must supply rules for building sources it contributes
src/vl6180x/%.o src/vl6180x/%.su: ../src/vl6180x/%.c src/vl6180x/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g -c -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

clean: clean-src-2f-vl6180x

clean-src-2f-vl6180x:
	-$(RM) ./src/vl6180x/vl6180x_api.d ./src/vl6180x/vl6180x_api.o ./src/vl6180x/vl6180x_api.su ./src/vl6180x/vl6180x_lib.d ./src/vl6180x/vl6180x_lib.o ./src/vl6180x/vl6180x_lib.su ./src/vl6180x/x-nucleo-6180xa1.d ./src/vl6180x/x-nucleo-6180xa1.o ./src/vl6180x/x-nucleo-6180xa1.su

.PHONY: clean-src-2f-vl6180x

