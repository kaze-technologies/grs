TARGET=libngham.a

BUILD_DIR := .

CC=cc
CFLAGS=-march=morello -mabi=aapcs -c -o
CFLAGST=-march=morello -mabi=aapcs -c


$(BUILD_DIR)/$(TARGET): $(BUILD_DIR)/ccsds_scrambler.o $(BUILD_DIR)/crc_ccitt.o $(BUILD_DIR)/fec.o $(BUILD_DIR)/ngham.o $(BUILD_DIR)/ngham_extension.o $(BUILD_DIR)/ngham_packets.o $(BUILD_DIR)/platform.o
	ar rcs $@ $^
	
$(BUILD_DIR)/ccsds_scrambler.o: ngham/ccsds_scrambler.c ngham/ccsds_scrambler.h
	$(CC) $(CFLAGS) $@ ngham/ccsds_scrambler.c
	
$(BUILD_DIR)/crc_ccitt.o: ngham/crc_ccitt.c ngham/crc_ccitt.h
	$(CC) $(CFLAGS) $@ ngham/crc_ccitt.c 

$(BUILD_DIR)/fec.o: ngham/fec.c ngham/fec.h
	$(CC) $(CFLAGS) $@ ngham/fec.c

$(BUILD_DIR)/ngham.o: ngham/ngham.c ngham/ngham.h
	$(CC) $(CFLAGS) $@ ngham/ngham.c

$(BUILD_DIR)/ngham_extension.o: ngham/ngham_extension.c ngham/ngham_extension.h
	$(CC) $(CFLAGS) $@ ngham/ngham_extension.c

$(BUILD_DIR)/ngham_packets.o: ngham/ngham_packets.c ngham/ngham_packets.h
	$(CC) $(CFLAGS) $@ ngham/ngham_packets.c

$(BUILD_DIR)/platform.o: ngham/platform/platform.c ngham/platform/platform.h
	$(CC) $(CFLAGS) $@ ngham/platform/platform.c
clean:
	rm $(BUILD_DIR)/*.o

