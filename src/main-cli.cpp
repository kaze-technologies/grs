/*
 * main.cpp
 * 
 * Copyright (C) 2017, Federal University of Santa Catarina.
 * 
 * This file is part of FloripaSat-GRS.
 * 
 * FloripaSat-GRS is free software: you can redistribute it
 * and/or modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 * 
 * FloripaSat-GRS is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with FloripaSat-GRS. If not, see <http://www.gnu.org/licenses/>.
 * 
 */

/**
 * \file main.cpp
 * 
 * \brief Main file.
 * 
 * \author Gabriel Mariano Marcelino <gabriel.mm8@gmail.com>
 * 
 * \version 1.0-dev
 * 
 * \date 05/05/2017
 * 
 * \defgroup fsat_grs FloripaSat GRS
 * \{
 */

//~ #include "fsat-grs.h"
#include "uart.h"
//~ #include "event_log.h"
//~ #include "log.h"
//~ #include "protocol_statistic.h"
#include "packet_data.h"
//~ #include "ngham_pkts.h"
//~ #include "read_log.h"
//~ #include "uplink_event.h"
//~ #include "payload_x_upload.h"
//~ #include "udp_decoder.h"
//~ #include "packets/beacon_data.h"
//~ #include "audio_decoder.h"
#include <iostream>

/**
 * \brief Uplink commands.
 */
enum uplink_cmds_t
{
    FSAT_GRS_UPLINK_PING = 0,                   /**< Ping. */
    FSAT_GRS_UPLINK_REQUEST,                    /**< Data request. */
    FSAT_GRS_UPLINK_ENTER_HIBERNATION,          /**< Enter hibernation. */
    FSAT_GRS_UPLINK_LEAVE_HIBERNATION,          /**< Leave hibernation. */
    FSAT_GRS_UPLINK_RESET_CHARGE,               /**< Reset EPS charge. */
    FSAT_GRS_UPLINK_BROADCAST_MESSAGE,          /**< Broadcast message. */
    FSAT_GRS_UPLINK_PAYLOAD_X_SWAP,             /**< Payload X swap. */
    FSAT_GRS_UPLINK_PAYLOAD_X_REQUEST_STATUS,   /**< Payload X request status. */
    FSAT_GRS_UPLINK_PAYLOAD_X_UPLOAD,           /**< Payload X upload. */
    FSAT_GRS_UPLINK_RUSH_ENABLE                 /**< RUSH enable. */
};

PacketData                      *beacon_data;
PacketData                      *telemetry_data;

void FSatGRS::RunGNURadioReceiver(uint8_t rx_type)
{
    string grc_cmd = "python2 -u ";

    if (this->CheckFile(FSAT_GRS_RX_GRC_SCRIPT))
    {
        grc_cmd += FSAT_GRS_RX_GRC_SCRIPT;
    }
    else
    {
        grc_cmd += FSAT_GRS_RX_GRC_SCRIPT_LOCAL;
    }

    switch(rx_type)
    {
        case FSAT_GRS_RX_BEACON:
            switch(combobox_beacon_sdr_dev->get_active_row_number())
            {
                case 0:     grc_cmd += " -d rtl=0";      break;
                case 1:     grc_cmd += " -d rtl=1";      break;
                case 2:     grc_cmd += " -d fcd=0";      break;
                case 3:     grc_cmd += " -d fcd=1";      break;
                case 4:     grc_cmd += " -d uhd=0";      break;
                case 5:     grc_cmd += " -d uhd=1";      break;
                default:    this->RaiseErrorMessage("Invalid SDR device!", "Check the SDR connection or model type.");
            }

            grc_cmd += " -f ";
            grc_cmd += entry_config_downlink_beacon_freq->get_text().c_str();

            grc_cmd += " -b ";
            grc_cmd += entry_config_downlink_beacon_baudrate->get_text().c_str();

            grc_cmd += " -p ";
            grc_cmd += entry_config_downlink_beacon_filter->get_text().c_str();

            grc_cmd += " -s ";
            grc_cmd += entry_config_downlink_beacon_sample_rate->get_text().c_str();
            
            grc_cmd += " -o ";
            grc_cmd += FSAT_GRS_GRC_BEACON_BIN;

            system(grc_cmd.c_str());

            break;
        case FSAT_GRS_RX_TELEMETRY:
            switch(combobox_telemetry_sdr_dev->get_active_row_number())
            {
                case 0:     grc_cmd += " -d rtl=0";      break;
                case 1:     grc_cmd += " -d rtl=1";      break;
                case 2:     grc_cmd += " -d fcd=0";      break;
                case 3:     grc_cmd += " -d fcd=1";      break;
                case 4:     grc_cmd += " -d uhd=0";      break;
                case 5:     grc_cmd += " -d uhd=1";      break;
                default:    this->RaiseErrorMessage("Invalid SDR device!", "Check the SDR connection or model type.");
            }

            grc_cmd += " -f ";
            grc_cmd += entry_config_downlink_telemetry_freq->get_text().c_str();

            grc_cmd += " -b ";
            grc_cmd += entry_config_downlink_telemetry_baudrate->get_text().c_str();

            grc_cmd += " -p ";
            grc_cmd += entry_config_downlink_telemetry_filter->get_text().c_str();

            grc_cmd += " -s ";
            grc_cmd += entry_config_downlink_telemetry_sample_rate->get_text().c_str();
            
            grc_cmd += " -o ";
            grc_cmd += FSAT_GRS_GRC_TELEMETRY_BIN;
            
            system(grc_cmd.c_str());

            break;
        default:
            this->RaiseErrorMessage("Invalid RX type!", "There is no receiver of this type.");
    }
}

/**
 * \fn main
 * 
 * \brief The main function.
 * 
 * \param argc Number of arguments passed in on the command line.
 * \param argv A pointer to an array of pointers to the arguments.
 * 
 * \return Returns the error code upon termination.
 */
int main(int argc, char *argv[])
{
    std::cout << "Welcome to the Floripasat Ground Station Command Line Tool" << std::endl;
    
    rx_type packet[999];
    //Init packet
    // packet = get_sample_packet(FILE_PATH)
    for(int x =0; x < PACKET_SIZE; ++i)
    {
		RunGNURadioReceiver()
	}
    
}

//! \} End of fsat_grs group
