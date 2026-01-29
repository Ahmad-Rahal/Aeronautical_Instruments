################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/MadgwickAHRS.c \
../src/anemo.c \
../src/drv_can.c \
../src/drv_i2c.c \
../src/drv_spi.c \
../src/drv_uart.c \
../src/dynamixel.c \
../src/hts221.c \
../src/lps25hb.c \
../src/main.c \
../src/mpu9250.c \
../src/stm32f1xx_hal_msp.c \
../src/stm32f1xx_it.c \
../src/syscalls.c \
../src/systemClock.c \
../src/system_stm32f1xx.c \
../src/tickTimer.c \
../src/util.c 

OBJS += \
./src/MadgwickAHRS.o \
./src/anemo.o \
./src/drv_can.o \
./src/drv_i2c.o \
./src/drv_spi.o \
./src/drv_uart.o \
./src/dynamixel.o \
./src/hts221.o \
./src/lps25hb.o \
./src/main.o \
./src/mpu9250.o \
./src/stm32f1xx_hal_msp.o \
./src/stm32f1xx_it.o \
./src/syscalls.o \
./src/systemClock.o \
./src/system_stm32f1xx.o \
./src/tickTimer.o \
./src/util.o 

C_DEPS += \
./src/MadgwickAHRS.d \
./src/anemo.d \
./src/drv_can.d \
./src/drv_i2c.d \
./src/drv_spi.d \
./src/drv_uart.d \
./src/dynamixel.d \
./src/hts221.d \
./src/lps25hb.d \
./src/main.d \
./src/mpu9250.d \
./src/stm32f1xx_hal_msp.d \
./src/stm32f1xx_it.d \
./src/syscalls.d \
./src/systemClock.d \
./src/system_stm32f1xx.d \
./src/tickTimer.d \
./src/util.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o src/%.su: ../src/%.c src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DSTM32 -DSTM32F1 -DSTM32F103RBTx -DNUCLEO_F103RB -DDEBUG -DSTM32F103xB -DUSE_HAL_DRIVER -c -I"/home/e2022/a2rahal/Bureau/CAN_project/WORKSPACE_RESCAPT_STM32CUBEIDE/WORKSPACE_RESCAPT_STM32CUBEIDE/rescapt/HAL_Driver/Inc/Legacy" -I"/home/e2022/a2rahal/Bureau/CAN_project/WORKSPACE_RESCAPT_STM32CUBEIDE/WORKSPACE_RESCAPT_STM32CUBEIDE/rescapt/src/vl6180x" -I"/home/e2022/a2rahal/Bureau/CAN_project/WORKSPACE_RESCAPT_STM32CUBEIDE/WORKSPACE_RESCAPT_STM32CUBEIDE/rescapt/Utilities/STM32F1xx_Nucleo" -I"/home/e2022/a2rahal/Bureau/CAN_project/WORKSPACE_RESCAPT_STM32CUBEIDE/WORKSPACE_RESCAPT_STM32CUBEIDE/rescapt/inc" -I"/home/e2022/a2rahal/Bureau/CAN_project/WORKSPACE_RESCAPT_STM32CUBEIDE/WORKSPACE_RESCAPT_STM32CUBEIDE/rescapt/CMSIS/device" -I"/home/e2022/a2rahal/Bureau/CAN_project/WORKSPACE_RESCAPT_STM32CUBEIDE/WORKSPACE_RESCAPT_STM32CUBEIDE/rescapt/CMSIS/core" -I"/home/e2022/a2rahal/Bureau/CAN_project/WORKSPACE_RESCAPT_STM32CUBEIDE/WORKSPACE_RESCAPT_STM32CUBEIDE/rescapt/HAL_Driver/Inc" -O0 -ffunction-sections -Wall -fcommon -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

clean: clean-src

clean-src:
	-$(RM) ./src/MadgwickAHRS.d ./src/MadgwickAHRS.o ./src/MadgwickAHRS.su ./src/anemo.d ./src/anemo.o ./src/anemo.su ./src/drv_can.d ./src/drv_can.o ./src/drv_can.su ./src/drv_i2c.d ./src/drv_i2c.o ./src/drv_i2c.su ./src/drv_spi.d ./src/drv_spi.o ./src/drv_spi.su ./src/drv_uart.d ./src/drv_uart.o ./src/drv_uart.su ./src/dynamixel.d ./src/dynamixel.o ./src/dynamixel.su ./src/hts221.d ./src/hts221.o ./src/hts221.su ./src/lps25hb.d ./src/lps25hb.o ./src/lps25hb.su ./src/main.d ./src/main.o ./src/main.su ./src/mpu9250.d ./src/mpu9250.o ./src/mpu9250.su ./src/stm32f1xx_hal_msp.d ./src/stm32f1xx_hal_msp.o ./src/stm32f1xx_hal_msp.su ./src/stm32f1xx_it.d ./src/stm32f1xx_it.o ./src/stm32f1xx_it.su ./src/syscalls.d ./src/syscalls.o ./src/syscalls.su ./src/systemClock.d ./src/systemClock.o ./src/systemClock.su ./src/system_stm32f1xx.d ./src/system_stm32f1xx.o ./src/system_stm32f1xx.su ./src/tickTimer.d ./src/tickTimer.o ./src/tickTimer.su ./src/util.d ./src/util.o ./src/util.su

.PHONY: clean-src

