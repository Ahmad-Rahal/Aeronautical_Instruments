################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Utilities/STM32F1xx_Nucleo/stm32f1xx_nucleo.c 

OBJS += \
./Utilities/STM32F1xx_Nucleo/stm32f1xx_nucleo.o 

C_DEPS += \
./Utilities/STM32F1xx_Nucleo/stm32f1xx_nucleo.d 


# Each subdirectory must supply rules for building sources it contributes
Utilities/STM32F1xx_Nucleo/%.o Utilities/STM32F1xx_Nucleo/%.su: ../Utilities/STM32F1xx_Nucleo/%.c Utilities/STM32F1xx_Nucleo/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g -c -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

clean: clean-Utilities-2f-STM32F1xx_Nucleo

clean-Utilities-2f-STM32F1xx_Nucleo:
	-$(RM) ./Utilities/STM32F1xx_Nucleo/stm32f1xx_nucleo.d ./Utilities/STM32F1xx_Nucleo/stm32f1xx_nucleo.o ./Utilities/STM32F1xx_Nucleo/stm32f1xx_nucleo.su

.PHONY: clean-Utilities-2f-STM32F1xx_Nucleo

