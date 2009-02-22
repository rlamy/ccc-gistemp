#!/usr/bin/env python
"""Module providing fix-up tables for the padjust.py program.

This is one of the programs where rounding issues produce slightly
different results ffrom the fortan. The fixups in these tables allow
the rounding differeneces to be 'fixed'.
"""
__docformat__ = "restructuredtext"


fixups = {
    12: {},
    13: {
        ('SUKUMO                         SB210', 263, 96): 95,
        ('SUKUMO                         SB210', 264, 66): 65,
        ('SUKUMO                         SB210', 265, 75): 74,
        ('SUKUMO                         SB210', 266, 89): 88,
        ('SUKUMO                         SB210', 267, 138): 137,
        ('SUKUMO                         SB210', 268, 188): 187,
        ('SUKUMO                         SB210', 269, 217): 216,
        ('SUKUMO                         SB210', 270, 265): 264,
        ('SUKUMO                         SB210', 271, 272): 271,
        ('SUKUMO                         SB210', 272, 218): 217,
        ('SUKUMO                         SB210', 273, 175): 174,
        ('SUKUMO                         SB210', 274, 148): 147,
        ('ORENBURG                       UB222', 120, -115): -116,
        ('ORENBURG                       UB222', 121, -171): -172,
        ('ORENBURG                       UB222', 122, -212): -213,
        ('ORENBURG                       UB222', 123, -68): -69,
        ('ORENBURG                       UB222', 124, 27): 26,
        ('ORENBURG                       UB222', 125, 149): 148,
        ('ORENBURG                       UB222', 126, 201): 200,
        ('ORENBURG                       UB222', 127, 246): 245,
        ('ORENBURG                       UB222', 128, 219): 218,
        ('ORENBURG                       UB222', 129, 111): 110,
        ('ORENBURG                       UB222', 130, 61): 60,
        ('ORENBURG                       UB222', 131, -27): -28,
        ('TERMEZ                         UC231', 461, 48): 47,
        ('TERMEZ                         UC231', 462, 47): 46,
        ('TERMEZ                         UC231', 463, 58): 57,
        ('TERMEZ                         UC231', 464, 87): 86,
        ('TERMEZ                         UC231', 465, 145): 144,
        ('TERMEZ                         UC231', 466, 232): 231,
        ('TERMEZ                         UC231', 467, 293): 292,
        ('TERMEZ                         UC231', 468, 304): 303,
        ('TERMEZ                         UC231', 469, 278): 277,
        ('TERMEZ                         UC231', 470, 221): 220,
        ('TERMEZ                         UC231', 471, 157): 156,
        ('TERMEZ                         UC231', 472, 108): 107,
        ('LA POCATIERE CDA,QU           2RC403', 770, -114): -113,
        ('LA POCATIERE CDA,QU           2RC403', 771, -93): -92,
        ('LA POCATIERE CDA,QU           2RC403', 772, -87): -86,
        ('LA POCATIERE CDA,QU           2RC403', 773, -41): -40,
        ('LA POCATIERE CDA,QU           2RC403', 774, 30): 31,
        ('LA POCATIERE CDA,QU           2RC403', 775, 114): 115,
        ('LA POCATIERE CDA,QU           2RC403', 776, 151): 152,
        ('LA POCATIERE CDA,QU           2RC403', 777, 172): 173,
        ('LA POCATIERE CDA,QU           2RC403', 778, 160): 161,
        ('LA POCATIERE CDA,QU           2RC403', 779, 123): 124,
        ('LA POCATIERE CDA,QU           2RC403', 780, 54): 55,
        ('LA POCATIERE CDA,QU           2RC403', 781, -3): -2,
        ('NORTH BAY,ONT                 3UC403', 756, -99): -98,
        ('NORTH BAY,ONT                 3UC403', 757, -125): -124,
        ('NORTH BAY,ONT                 3UC403', 758, -97): -96,
        ('NORTH BAY,ONT                 3UC403', 759, -41): -40,
        ('NORTH BAY,ONT                 3UC403', 760, 44): 45,
        ('NORTH BAY,ONT                 3UC403', 761, 121): 122,
        ('NORTH BAY,ONT                 3UC403', 762, 155): 156,
        ('NORTH BAY,ONT                 3UC403', 763, 178): 179,
        ('NORTH BAY,ONT                 3UC403', 764, 157): 158,
        ('NORTH BAY,ONT                 3UC403', 765, 118): 119,
        ('NORTH BAY,ONT                 3UC403', 766, 64): 65,
        ('NORTH BAY,ONT                 3UC403', 767, -41): -40,
        ('TIMMINS,ONT.                  2SB403', 104, -167): -168,
        ('TIMMINS,ONT.                  2SB403', 105, -121): -122,
        ('TIMMINS,ONT.                  2SB403', 106, -132): -133,
        ('TIMMINS,ONT.                  2SB403', 107, -113): -114,
        ('TIMMINS,ONT.                  2SB403', 108, 13): 12,
        ('TIMMINS,ONT.                  2SB403', 109, 117): 116,
        ('TIMMINS,ONT.                  2SB403', 110, 132): 131,
        ('TIMMINS,ONT.                  2SB403', 111, 182): 181,
        ('TIMMINS,ONT.                  2SB403', 112, 133): 132,
        ('TIMMINS,ONT.                  2SB403', 113, 99): 98,
        ('TIMMINS,ONT.                  2SB403', 114, 38): 37,
        ('TIMMINS,ONT.                  2SB403', 115, -42): -43,
        ('SUMMERLAND CDA,BC             2RB403', 647, -3): -4,
        ('SUMMERLAND CDA,BC             2RB403', 648, -38): -39,
        ('SUMMERLAND CDA,BC             2RB403', 649, 14): 13,
        ('SUMMERLAND CDA,BC             2RB403', 650, 42): 41,
        ('SUMMERLAND CDA,BC             2RB403', 651, 74): 73,
        ('SUMMERLAND CDA,BC             2RB403', 652, 131): 130,
        ('SUMMERLAND CDA,BC             2RB403', 653, 196): 195,
        ('SUMMERLAND CDA,BC             2RB403', 654, 220): 219,
        ('SUMMERLAND CDA,BC             2RB403', 655, 210): 209,
        ('SUMMERLAND CDA,BC             2RB403', 656, 127): 126,
        ('SUMMERLAND CDA,BC             2RB403', 657, 77): 76,
        ('SUMMERLAND CDA,BC             2RB403', 658, 4): 3,
        ('SAVANNAH/MUNI                 3UC425', 91, 100): 101,
        ('SAVANNAH/MUNI                 3UC425', 92, 88): 89,
        ('SAVANNAH/MUNI                 3UC425', 93, 90): 91,
        ('SAVANNAH/MUNI                 3UC425', 94, 140): 141,
        ('SAVANNAH/MUNI                 3UC425', 95, 195): 196,
        ('SAVANNAH/MUNI                 3UC425', 96, 226): 227,
        ('SAVANNAH/MUNI                 3UC425', 97, 253): 254,
        ('SAVANNAH/MUNI                 3UC425', 98, 274): 275,
        ('SAVANNAH/MUNI                 3UC425', 99, 284): 285,
        ('SAVANNAH/MUNI                 3UC425', 100, 258): 259,
        ('SAVANNAH/MUNI                 3UC425', 101, 215): 216,
        ('SAVANNAH/MUNI                 3UC425', 102, 156): 157,
        ('TROY                          2SC425', 174, 141): 142,
        ('TROY                          2SC425', 175, 124): 125,
        ('TROY                          2SC425', 176, 105): 106,
        ('TROY                          2SC425', 177, 133): 134,
        ('TROY                          2SC425', 178, 180): 181,
        ('TROY                          2SC425', 179, 213): 214,
        ('TROY                          2SC425', 180, 258): 259,
        ('TROY                          2SC425', 181, 260): 261,
        ('TROY                          2SC425', 182, 266): 267,
        ('TROY                          2SC425', 183, 255): 256,
        ('TROY                          2SC425', 184, 181): 182,
        ('TROY                          2SC425', 185, 118): 119,
        ('GAINESVILLE 5ENE              2SA425', 479, 92): 93,
        ('GAINESVILLE 5ENE              2SA425', 480, -6): -5,
        ('GAINESVILLE 5ENE              2SA425', 481, 123): 124,
        ('GAINESVILLE 5ENE              2SA425', 482, 117): 118,
        ('GAINESVILLE 5ENE              2SA425', 483, 206): 207,
        ('GAINESVILLE 5ENE              2SA425', 484, 235): 236,
        ('GAINESVILLE 5ENE              2SA425', 485, 272): 273,
        ('GAINESVILLE 5ENE              2SA425', 486, 308): 309,
        ('GAINESVILLE 5ENE              2SA425', 487, 300): 301,
        ('GAINESVILLE 5ENE              2SA425', 488, 275): 276,
        ('GAINESVILLE 5ENE              2SA425', 489, 188): 189,
        ('GAINESVILLE 5ENE              2SA425', 490, 123): 124,
        ('SMITHFIELD                    3RC425', 617, 63): 64,
        ('SMITHFIELD                    3RC425', 618, 41): 42,
        ('SMITHFIELD                    3RC425', 619, 31): 32,
        ('SMITHFIELD                    3RC425', 620, 113): 114,
        ('SMITHFIELD                    3RC425', 621, 155): 156,
        ('SMITHFIELD                    3RC425', 622, 211): 212,
        ('SMITHFIELD                    3RC425', 623, 249): 250,
        ('SMITHFIELD                    3RC425', 624, 268): 269,
        ('SMITHFIELD                    3RC425', 625, 245): 246,
        ('SMITHFIELD                    3RC425', 626, 227): 228,
        ('SMITHFIELD                    3RC425', 627, 161): 162,
        ('SMITHFIELD                    3RC425', 628, 105): 106,
        ('CORINTH CITY                  3SC425', 32, 54): 53,
        ('CORINTH CITY                  3SC425', 33, 56): 55,
        ('CORINTH CITY                  3SC425', 34, 35): 34,
        ('CORINTH CITY                  3SC425', 35, 102): 101,
        ('CORINTH CITY                  3SC425', 36, 165): 164,
        ('CORINTH CITY                  3SC425', 37, 206): 205,
        ('CORINTH CITY                  3SC425', 38, 229): 228,
        ('CORINTH CITY                  3SC425', 39, 269): 268,
        ('CORINTH CITY                  3SC425', 40, 275): 274,
        ('KINGMAN 2                     3SC425', 156, 37): 38,
        ('KINGMAN 2                     3SC425', 157, 33): 34,
        ('KINGMAN 2                     3SC425', 158, 70): 71,
        ('KINGMAN 2                     3SC425', 161, 160): 161,
        ('KINGMAN 2                     3SC425', 166, 193): 194,
        ('KINGMAN 2                     3SC425', 167, 118): 119,
        ('SPENCER 1SE                   2RB425', 1126, -10): -11,
        ('SPENCER 1SE                   2RB425', 1127, -5): -6,
        ('SPENCER 1SE                   2RB425', 1128, 28): 27,
        ('SPENCER 1SE                   2RB425', 1129, 60): 59,
        ('SPENCER 1SE                   2RB425', 1130, 132): 131,
        ('SPENCER 1SE                   2RB425', 1131, 170): 169,
        ('SPENCER 1SE                   2RB425', 1132, 214): 213,
        ('SPENCER 1SE                   2RB425', 1133, 246): 245,
        ('SPENCER 1SE                   2RB425', 1134, 213): 212,
        ('SPENCER 1SE                   2RB425', 1135, 193): 192,
        ('SPENCER 1SE                   2RB425', 1136, 132): 131,
        ('SPENCER 1SE                   2RB425', 1137, 64): 63,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 551, -6): -5,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 552, -46): -45,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 553, 4): 5,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 554, 43): 44,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 555, 121): 122,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 556, 118): 119,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 557, 207): 208,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 558, 221): 222,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 559, 201): 202,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 560, 159): 160,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 561, 101): 102,
        ('ELKINS/RANDOLPH CO ARPT       2RB425', 562, 82): 83,
        ('LOUISVILLE/                   3UC425', 719, 43): 42,
        ('LOUISVILLE/                   3UC425', 720, -58): -59,
        ('LOUISVILLE/                   3UC425', 721, 24): 23,
        ('LOUISVILLE/                   3UC425', 722, 68): 67,
        ('LOUISVILLE/                   3UC425', 723, 127): 126,
        ('LOUISVILLE/                   3UC425', 724, 176): 175,
        ('LOUISVILLE/                   3UC425', 725, 244): 243,
        ('LOUISVILLE/                   3UC425', 726, 263): 262,
        ('LOUISVILLE/                   3UC425', 727, 265): 264,
        ('LOUISVILLE/                   3UC425', 728, 207): 206,
        ('LOUISVILLE/                   3UC425', 729, 179): 178,
        ('LOUISVILLE/                   3UC425', 730, 87): 86,
        ('WAVERLY                       2RC425', 30, 8): 9,
        ('WAVERLY                       2RC425', 31, -41): -40,
        ('WAVERLY                       2RC425', 32, -22): -21,
        ('WAVERLY                       2RC425', 33, 41): 42,
        ('WAVERLY                       2RC425', 35, 182): 183,
        ('WAVERLY                       2RC425', 36, 202): 203,
        ('WAVERLY                       2RC425', 37, 222): 223,
        ('WAVERLY                       2RC425', 38, 213): 214,
        ('WAVERLY                       2RC425', 39, 192): 193,
        ('WAVERLY                       2RC425', 40, 115): 116,
        ('WAVERLY                       2RC425', 41, 31): 32,
        ('WICHITA/MID-                  3UC425', 377, -19): -18,
        ('WICHITA/MID-                  3UC425', 378, 0): 1,
        ('WICHITA/MID-                  3UC425', 379, 30): 31,
        ('WICHITA/MID-                  3UC425', 380, 86): 87,
        ('WICHITA/MID-                  3UC425', 381, 108): 109,
        ('WICHITA/MID-                  3UC425', 382, 188): 189,
        ('WICHITA/MID-                  3UC425', 383, 233): 234,
        ('WICHITA/MID-                  3UC425', 384, 260): 261,
        ('WICHITA/MID-                  3UC425', 385, 238): 239,
        ('WICHITA/MID-                  3UC425', 386, 220): 221,
        ('WICHITA/MID-                  3UC425', 387, 173): 174,
        ('WICHITA/MID-                  3UC425', 388, 51): 52,
        ('CASTLE/AFB                    3RC425', 191, 96): 95,
        ('CASTLE/AFB                    3RC425', 192, 77): 76,
        ('CASTLE/AFB                    3RC425', 193, 91): 90,
        ('CASTLE/AFB                    3RC425', 194, 117): 116,
        ('CASTLE/AFB                    3RC425', 195, 149): 148,
        ('CASTLE/AFB                    3RC425', 196, 189): 188,
        ('CASTLE/AFB                    3RC425', 197, 208): 207,
        ('CASTLE/AFB                    3RC425', 199, 248): 247,
        ('CASTLE/AFB                    3RC425', 200, 203): 202,
        ('CASTLE/AFB                    3RC425', 201, 192): 191,
        ('CASTLE/AFB                    3RC425', 202, 125): 124,
        ('AUBURN                        2SB425', 39, -33): -32,
        ('AUBURN                        2SB425', 40, -48): -47,
        ('AUBURN                        2SB425', 41, -84): -83,
        ('AUBURN                        2SB425', 42, 0): 1,
        ('AUBURN                        2SB425', 43, 84): 85,
        ('AUBURN                        2SB425', 44, 149): 150,
        ('AUBURN                        2SB425', 48, 166): 167,
        ('AUBURN                        2SB425', 49, 98): 99,
        ('AUBURN                        2SB425', 50, -2): -1,
        ('PEORIA/GREATE                 3UC425', 263, -40): -41,
        ('PEORIA/GREATE                 3UC425', 264, -32): -33,
        ('PEORIA/GREATE                 3UC425', 265, -60): -61,
        ('PEORIA/GREATE                 3UC425', 266, 53): 52,
        ('PEORIA/GREATE                 3UC425', 267, 101): 100,
        ('PEORIA/GREATE                 3UC425', 268, 193): 192,
        ('PEORIA/GREATE                 3UC425', 269, 200): 199,
        ('PEORIA/GREATE                 3UC425', 270, 237): 236,
        ('PEORIA/GREATE                 3UC425', 271, 214): 213,
        ('PEORIA/GREATE                 3UC425', 272, 165): 164,
        ('PEORIA/GREATE                 3UC425', 273, 129): 128,
        ('PEORIA/GREATE                 3UC425', 274, 88): 87,
        ('UPPER SANDUSKY                2RC425', 1177, -20): -19,
        ('UPPER SANDUSKY                2RC425', 1178, -71): -70,
        ('UPPER SANDUSKY                2RC425', 1179, -12): -11,
        ('UPPER SANDUSKY                2RC425', 1180, 23): 24,
        ('UPPER SANDUSKY                2RC425', 1181, 107): 108,
        ('UPPER SANDUSKY                2RC425', 1182, 139): 140,
        ('UPPER SANDUSKY                2RC425', 1183, 211): 212,
        ('UPPER SANDUSKY                2RC425', 1184, 228): 229,
        ('UPPER SANDUSKY                2RC425', 1185, 211): 212,
        ('UPPER SANDUSKY                2RC425', 1186, 167): 168,
        ('UPPER SANDUSKY                2RC425', 1187, 96): 97,
        ('UPPER SANDUSKY                2RC425', 1188, 49): 50,
        ('INDIANOLA                     2SC425', 852, -72): -73,
        ('INDIANOLA                     2SC425', 853, -104): -105,
        ('INDIANOLA                     2SC425', 854, -50): -51,
        ('INDIANOLA                     2SC425', 855, -14): -15,
        ('INDIANOLA                     2SC425', 856, 85): 84,
        ('INDIANOLA                     2SC425', 857, 190): 189,
        ('INDIANOLA                     2SC425', 858, 199): 198,
        ('INDIANOLA                     2SC425', 859, 216): 215,
        ('INDIANOLA                     2SC425', 860, 215): 214,
        ('INDIANOLA                     2SC425', 861, 158): 157,
        ('INDIANOLA                     2SC425', 862, 131): 130,
        ('INDIANOLA                     2SC425', 863, 35): 34,
        ('FORT BRAGG 5N                 2RB425', 44, 84): 85,
        ('FORT BRAGG 5N                 2RB425', 45, 85): 86,
        ('FORT BRAGG 5N                 2RB425', 46, 71): 72,
        ('FORT BRAGG 5N                 2RB425', 47, 68): 69,
        ('FORT BRAGG 5N                 2RB425', 48, 101): 102,
        ('FORT BRAGG 5N                 2RB425', 49, 104): 105,
        ('FORT BRAGG 5N                 2RB425', 50, 129): 130,
        ('FORT BRAGG 5N                 2RB425', 51, 123): 124,
        ('FORT BRAGG 5N                 2RB425', 52, 133): 134,
        ('FORT BRAGG 5N                 2RB425', 53, 137): 138,
        ('FORT BRAGG 5N                 2RB425', 54, 121): 122,
        ('FORT BRAGG 5N                 2RB425', 55, 90): 91,
        ('WAUSAU              USA       3SC425', 404, -44): -43,
        ('WAUSAU              USA       3SC425', 405, -168): -167,
        ('WAUSAU              USA       3SC425', 406, -128): -127,
        ('WAUSAU              USA       3SC425', 407, -2): -1,
        ('WAUSAU              USA       3SC425', 408, 76): 77,
        ('WAUSAU              USA       3SC425', 409, 111): 112,
        ('WAUSAU              USA       3SC425', 410, 172): 173,
        ('WAUSAU              USA       3SC425', 411, 214): 215,
        ('WAUSAU              USA       3SC425', 412, 192): 193,
        ('WAUSAU              USA       3SC425', 413, 148): 149,
        ('WAUSAU              USA       3SC425', 414, 83): 84,
        ('WAUSAU              USA       3SC425', 415, -23): -22,
        ('MENNO                         2RC425', 271, -27): -28,
        ('MENNO                         2RC425', 272, -24): -25,
        ('MENNO                         2RC425', 273, -59): -60,
        ('MENNO                         2RC425', 274, -5): -6,
        ('MENNO                         2RC425', 276, 147): 146,
        ('MENNO                         2RC425', 277, 203): 202,
        ('MENNO                         2RC425', 278, 237): 236,
        ('MENNO                         2RC425', 282, -27): -28,
        ('BUFFALO BILL DAM              2RA425', 59, -87): -86,
        ('BUFFALO BILL DAM              2RA425', 60, -38): -37,
        ('BUFFALO BILL DAM              2RA425', 61, -53): -52,
        ('BUFFALO BILL DAM              2RA425', 62, 88): 89,
        ('BUFFALO BILL DAM              2RA425', 63, 115): 116,
        ('BUFFALO BILL DAM              2RA425', 64, 119): 120,
        ('BUFFALO BILL DAM              2RA425', 65, 169): 170,
        ('BUFFALO BILL DAM              2RA425', 66, 208): 209,
        ('BUFFALO BILL DAM              2RA425', 67, 180): 181,
        ('BUFFALO BILL DAM              2RA425', 68, 149): 150,
        ('BUFFALO BILL DAM              2RA425', 69, 114): 115,
        ('BUFFALO BILL DAM              2RA425', 70, 27): 28,
        ('LONGVIEW                      3SC425', 911, 45): 46,
        ('LONGVIEW                      3SC425', 912, 52): 53,
        ('LONGVIEW                      3SC425', 913, 56): 57,
        ('LONGVIEW                      3SC425', 914, 84): 85,
        ('LONGVIEW                      3SC425', 915, 91): 92,
        ('LONGVIEW                      3SC425', 916, 141): 142,
        ('LONGVIEW                      3SC425', 917, 152): 153,
        ('LONGVIEW                      3SC425', 919, 193): 194,
        ('LONGVIEW                      3SC425', 920, 169): 170,
        ('LONGVIEW                      3SC425', 922, 90): 91,
        ('PINE RIVER DAM                2RB425', 153, -104): -103,
        ('PINE RIVER DAM                2RB425', 154, -111): -110,
        ('PINE RIVER DAM                2RB425', 155, -177): -176,
        ('PINE RIVER DAM                2RB425', 156, -79): -78,
        ('PINE RIVER DAM                2RB425', 157, 95): 96,
        ('PINE RIVER DAM                2RB425', 158, 134): 135,
        ('PINE RIVER DAM                2RB425', 159, 187): 188,
        ('PINE RIVER DAM                2RB425', 160, 191): 192,
        ('PINE RIVER DAM                2RB425', 161, 227): 228,
        ('PINE RIVER DAM                2RB425', 162, 145): 146,
        ('PINE RIVER DAM                2RB425', 163, 122): 123,
        ('PINE RIVER DAM                2RB425', 164, -45): -44,
        ('PINE RIVER DAM                2RB425', 1005, -124): -123,
        ('PINE RIVER DAM                2RB425', 1006, -182): -181,
        ('PINE RIVER DAM                2RB425', 1007, -104): -103,
        ('PINE RIVER DAM                2RB425', 1008, -42): -41,
        ('PINE RIVER DAM                2RB425', 1009, 57): 58,
        ('PINE RIVER DAM                2RB425', 1010, 107): 108,
        ('PINE RIVER DAM                2RB425', 1011, 197): 198,
        ('PINE RIVER DAM                2RB425', 1012, 182): 183,
        ('PINE RIVER DAM                2RB425', 1013, 181): 182,
        ('PINE RIVER DAM                2RB425', 1014, 146): 147,
        ('PINE RIVER DAM                2RB425', 1015, 97): 98,
        ('PINE RIVER DAM                2RB425', 1016, -13): -12,
        ('PINE RIVER DAM                2RB425', 1125, -112): -111,
        ('PINE RIVER DAM                2RB425', 1126, -113): -112,
        ('PINE RIVER DAM                2RB425', 1127, -76): -75,
        ('PINE RIVER DAM                2RB425', 1128, -6): -5,
        ('PINE RIVER DAM                2RB425', 1129, 70): 71,
        ('PINE RIVER DAM                2RB425', 1130, 118): 119,
        ('PINE RIVER DAM                2RB425', 1131, 171): 172,
        ('PINE RIVER DAM                2RB425', 1132, 206): 207,
        ('PINE RIVER DAM                2RB425', 1133, 197): 198,
        ('PINE RIVER DAM                2RB425', 1134, 132): 133,
        ('PINE RIVER DAM                2RB425', 1135, 57): 58,
        ('PINE RIVER DAM                2RB425', 1136, 10): 11,
        ('PINE RIVER DAM                2RB425', 1245, -118): -117,
        ('PINE RIVER DAM                2RB425', 1246, -151): -150,
        ('PINE RIVER DAM                2RB425', 1247, -70): -69,
        ('PINE RIVER DAM                2RB425', 1248, -24): -23,
        ('PINE RIVER DAM                2RB425', 1249, 74): 75,
        ('PINE RIVER DAM                2RB425', 1250, 152): 153,
        ('PINE RIVER DAM                2RB425', 1251, 204): 205,
        ('PINE RIVER DAM                2RB425', 1252, 206): 207,
        ('PINE RIVER DAM                2RB425', 1253, 214): 215,
        ('PINE RIVER DAM                2RB425', 1254, 134): 135,
        ('PINE RIVER DAM                2RB425', 1255, 61): 62,
        ('PINE RIVER DAM                2RB425', 1256, -56): -55,
        ('PINE RIVER DAM                2RB425', 1365, -171): -170,
        ('PINE RIVER DAM                2RB425', 1366, -94): -93,
        ('PINE RIVER DAM                2RB425', 1367, -162): -161,
        ('PINE RIVER DAM                2RB425', 1368, -45): -44,
        ('PINE RIVER DAM                2RB425', 1369, 49): 50,
        ('PINE RIVER DAM                2RB425', 1370, 135): 136,
        ('PINE RIVER DAM                2RB425', 1371, 184): 185,
        ('PINE RIVER DAM                2RB425', 1372, 214): 215,
        ('PINE RIVER DAM                2RB425', 1373, 214): 215,
        ('PINE RIVER DAM                2RB425', 1374, 140): 141,
        ('PINE RIVER DAM                2RB425', 1375, 67): 68,
        ('PINE RIVER DAM                2RB425', 1376, 49): 50,
        ('FORT ASSINNIBOINE             2RA425', 887, -92): -93,
        ('FORT ASSINNIBOINE             2RA425', 888, -99): -100,
        ('FORT ASSINNIBOINE             2RA425', 889, 31): 30,
        ('FORT ASSINNIBOINE             2RA425', 890, 14): 13,
        ('FORT ASSINNIBOINE             2RA425', 891, 79): 78,
        ('FORT ASSINNIBOINE             2RA425', 892, 120): 119,
        ('FORT ASSINNIBOINE             2RA425', 893, 166): 165,
        ('FORT ASSINNIBOINE             2RA425', 894, 210): 209,
        ('FORT ASSINNIBOINE             2RA425', 895, 229): 228,
        ('FORT ASSINNIBOINE             2RA425', 896, 152): 151,
        ('FORT ASSINNIBOINE             2RA425', 897, 59): 58,
        ('FORT ASSINNIBOINE             2RA425', 898, -12): -13,
        ('OTTAWA 4SW                    2SB425', 657, -38): -37,
        ('OTTAWA 4SW                    2SB425', 658, -29): -28,
        ('OTTAWA 4SW                    2SB425', 659, -18): -17,
        ('OTTAWA 4SW                    2SB425', 660, 27): 28,
        ('OTTAWA 4SW                    2SB425', 661, 93): 94,
        ('OTTAWA 4SW                    2SB425', 662, 164): 165,
        ('OTTAWA 4SW                    2SB425', 663, 222): 223,
        ('OTTAWA 4SW                    2SB425', 664, 218): 219,
        ('OTTAWA 4SW                    2SB425', 665, 224): 225,
        ('OTTAWA 4SW                    2SB425', 666, 182): 183,
        ('OTTAWA 4SW                    2SB425', 667, 152): 153,
        ('OTTAWA 4SW                    2SB425', 668, 38): 39,
        ('GLENN DALE BELL STN           3UC425', 0, 15): 14,
        ('GLENN DALE BELL STN           3UC425', 1, 29): 28,
        ('GLENN DALE BELL STN           3UC425', 2, 130): 129,
        ('GLENN DALE BELL STN           3UC425', 3, 148): 147,
        ('GLENN DALE BELL STN           3UC425', 4, 164): 163,
        ('GLENN DALE BELL STN           3UC425', 5, 226): 225,
        ('GLENN DALE BELL STN           3UC425', 6, 253): 252,
        ('GLENN DALE BELL STN           3UC425', 7, 216): 215,
        ('GLENN DALE BELL STN           3UC425', 8, 228): 227,
        ('GLENN DALE BELL STN           3UC425', 9, 126): 125,
        ('GLENN DALE BELL STN           3UC425', 10, 83): 82,
        ('FARMINGTON                    2SC425', 659, 6): 7,
        ('FARMINGTON                    2SC425', 660, 9): 10,
        ('FARMINGTON                    2SC425', 661, 39): 40,
        ('FARMINGTON                    2SC425', 662, 37): 38,
        ('FARMINGTON                    2SC425', 663, 121): 122,
        ('FARMINGTON                    2SC425', 664, 175): 176,
        ('FARMINGTON                    2SC425', 665, 245): 246,
        ('FARMINGTON                    2SC425', 666, 261): 262,
        ('FARMINGTON                    2SC425', 667, 256): 257,
        ('FARMINGTON                    2SC425', 668, 181): 182,
        ('FARMINGTON                    2SC425', 669, 122): 123,
        ('FARMINGTON                    2SC425', 670, 59): 60,
        ('LARISSA                        UC618', 408, 59): 58,
        ('LARISSA                        UC618', 409, 64): 63,
        ('LARISSA                        UC618', 410, 69): 68,
        ('LARISSA                        UC618', 411, 91): 90,
        ('LARISSA                        UC618', 412, 148): 147,
        ('LARISSA                        UC618', 413, 194): 193,
        ('LARISSA                        UC618', 414, 254): 253,
        ('LARISSA                        UC618', 415, 258): 257,
        ('LARISSA                        UC618', 416, 249): 248,
        ('LARISSA                        UC618', 417, 204): 203,
        ('LARISSA                        UC618', 418, 128): 127,
        ('LARISSA                        UC618', 419, 102): 101,
        ('STAVANGER/SOL                  UC634', 71, 38): 39,
        ('STAVANGER/SOL                  UC634', 72, 29): 30,
        ('STAVANGER/SOL                  UC634', 73, 17): 18,
        ('STAVANGER/SOL                  UC634', 74, 42): 43,
        ('STAVANGER/SOL                  UC634', 75, 55): 56,
        ('STAVANGER/SOL                  UC634', 76, 84): 85,
        ('STAVANGER/SOL                  UC634', 77, 109): 110,
        ('STAVANGER/SOL                  UC634', 78, 138): 139,
        ('STAVANGER/SOL                  UC634', 79, 136): 137,
        ('STAVANGER/SOL                  UC634', 80, 105): 106,
        ('STAVANGER/SOL                  UC634', 81, 89): 90,
        ('STAVANGER/SOL                  UC634', 82, 44): 45,
        ('KRALJEVO                       SB639', 118, -6): -5,
        ('KRALJEVO                       SB639', 119, 5): 6,
        ('KRALJEVO                       SB639', 120, 1): 2,
        ('KRALJEVO                       SB639', 121, 37): 38,
        ('KRALJEVO                       SB639', 122, 119): 120,
        ('KRALJEVO                       SB639', 123, 166): 167,
        ('KRALJEVO                       SB639', 124, 178): 179,
        ('KRALJEVO                       SB639', 125, 206): 207,
        ('KRALJEVO                       SB639', 126, 220): 221,
        ('KRALJEVO                       SB639', 127, 171): 172,
        ('KRALJEVO                       SB639', 128, 124): 125,
        ('KRALJEVO                       SB639', 129, 82): 83,
        ('KUTAHYA                        UB649', 47, 44): 43,
        ('KUTAHYA                        UB649', 48, 16): 15,
        ('KUTAHYA                        UB649', 49, 0): -1,
        ('KUTAHYA                        UB649', 50, 61): 60,
        ('KUTAHYA                        UB649', 51, 93): 92,
        ('KUTAHYA                        UB649', 52, 134): 133,
        ('KUTAHYA                        UB649', 53, 189): 188,
        ('KUTAHYA                        UB649', 54, 196): 195,
        ('KUTAHYA                        UB649', 55, 198): 197,
        ('KUTAHYA                        UB649', 56, 178): 177,
        ('KUTAHYA                        UB649', 57, 91): 90,
        ('KUTAHYA                        UB649', 58, 77): 76,
        ("UMAN'                          UC650", 371, -18): -17,
        ("UMAN'                          UC650", 372, -60): -59,
        ("UMAN'                          UC650", 373, -112): -111,
        ("UMAN'                          UC650", 374, -35): -34,
        ("UMAN'                          UC650", 375, 84): 85,
        ("UMAN'                          UC650", 376, 124): 125,
        ("UMAN'                          UC650", 377, 181): 182,
        ("UMAN'                          UC650", 378, 181): 182,
        ("UMAN'                          UC650", 379, 200): 201,
        ("UMAN'                          UC650", 380, 140): 141,
        ("UMAN'                          UC650", 381, 93): 94,
        ("UMAN'                          UC650", 382, 52): 53,
    },
    14: {
        ('WEST PALM BEA                 3UC425', 395, 187): 188,
        ('WEST PALM BEA                 3UC425', 396, 149): 150,
        ('WEST PALM BEA                 3UC425', 397, 199): 200,
        ('WEST PALM BEA                 3UC425', 398, 200): 201,
        ('WEST PALM BEA                 3UC425', 399, 244): 245,
        ('WEST PALM BEA                 3UC425', 400, 259): 260,
        ('WEST PALM BEA                 3UC425', 401, 286): 287,
        ('WEST PALM BEA                 3UC425', 402, 290): 291,
        ('WEST PALM BEA                 3UC425', 403, 284): 285,
        ('WEST PALM BEA                 3UC425', 404, 274): 275,
        ('WEST PALM BEA                 3UC425', 405, 257): 258,
        ('WEST PALM BEA                 3UC425', 406, 200): 201,
        ('BARBERS POINT/NAS              UC425', 106, 232): 233,
        ('BARBERS POINT/NAS              UC425', 107, 220): 221,
        ('BARBERS POINT/NAS              UC425', 108, 222): 223,
        ('BARBERS POINT/NAS              UC425', 109, 214): 215,
        ('BARBERS POINT/NAS              UC425', 110, 229): 230,
        ('BARBERS POINT/NAS              UC425', 111, 235): 236,
        ('BARBERS POINT/NAS              UC425', 112, 251): 252,
        ('BARBERS POINT/NAS              UC425', 113, 255): 256,
        ('BARBERS POINT/NAS              UC425', 114, 263): 264,
        ('BARBERS POINT/NAS              UC425', 115, 265): 266,
        ('BARBERS POINT/NAS              UC425', 116, 253): 254,
        ('BARBERS POINT/NAS              UC425', 117, 241): 242,
    },
    15: {
        ('ENCARNACION                    SC308', 323, 279): 280,
        ('ENCARNACION                    SC308', 324, 267): 268,
        ('ENCARNACION                    SC308', 325, 262): 263,
        ('ENCARNACION                    SC308', 326, 249): 250,
        ('ENCARNACION                    SC308', 327, 181): 182,
        ('ENCARNACION                    SC308', 328, 157): 158,
        ('ENCARNACION                    SC308', 329, 164): 165,
        ('ENCARNACION                    SC308', 330, 170): 171,
        ('ENCARNACION                    SC308', 331, 176): 177,
        ('ENCARNACION                    SC308', 332, 173): 174,
        ('ENCARNACION                    SC308', 333, 222): 223,
        ('ENCARNACION                    SC308', 334, 265): 266,
    },
    16: {
        ('MELBOURNE                      UC501', 803, 189): 190,
        ('MELBOURNE                      UC501', 804, 204): 205,
        ('MELBOURNE                      UC501', 805, 229): 230,
        ('MELBOURNE                      UC501', 806, 194): 195,
        ('MELBOURNE                      UC501', 807, 162): 163,
        ('MELBOURNE                      UC501', 808, 147): 148,
        ('MELBOURNE                      UC501', 809, 111): 112,
        ('MELBOURNE                      UC501', 810, 107): 108,
        ('MELBOURNE                      UC501', 811, 103): 104,
        ('MELBOURNE                      UC501', 812, 126): 127,
        ('MELBOURNE                      UC501', 813, 143): 144,
        ('MELBOURNE                      UC501', 814, 155): 156,
        ('MELBOURNE                      UC501', 923, 175): 176,
        ('MELBOURNE                      UC501', 924, 191): 192,
        ('MELBOURNE                      UC501', 925, 201): 202,
        ('MELBOURNE                      UC501', 926, 179): 180,
        ('MELBOURNE                      UC501', 927, 157): 158,
        ('MELBOURNE                      UC501', 928, 127): 128,
        ('MELBOURNE                      UC501', 929, 139): 140,
        ('MELBOURNE                      UC501', 930, 96): 97,
        ('MELBOURNE                      UC501', 931, 107): 108,
        ('MELBOURNE                      UC501', 932, 124): 125,
        ('MELBOURNE                      UC501', 933, 142): 143,
        ('MELBOURNE                      UC501', 934, 165): 166,
        ('MELBOURNE                      UC501', 1043, 185): 186,
        ('MELBOURNE                      UC501', 1044, 191): 192,
        ('MELBOURNE                      UC501', 1045, 221): 222,
        ('MELBOURNE                      UC501', 1046, 188): 189,
        ('MELBOURNE                      UC501', 1047, 168): 169,
        ('MELBOURNE                      UC501', 1048, 135): 136,
        ('MELBOURNE                      UC501', 1049, 111): 112,
        ('MELBOURNE                      UC501', 1050, 103): 104,
        ('MELBOURNE                      UC501', 1051, 105): 106,
        ('MELBOURNE                      UC501', 1052, 127): 128,
        ('MELBOURNE                      UC501', 1053, 158): 159,
        ('MELBOURNE                      UC501', 1054, 174): 175,
        ('MELBOURNE                      UC501', 1163, 194): 195,
        ('MELBOURNE                      UC501', 1164, 203): 204,
        ('MELBOURNE                      UC501', 1165, 209): 210,
        ('MELBOURNE                      UC501', 1166, 188): 189,
        ('MELBOURNE                      UC501', 1167, 150): 151,
        ('MELBOURNE                      UC501', 1168, 131): 132,
        ('MELBOURNE                      UC501', 1169, 106): 107,
        ('MELBOURNE                      UC501', 1170, 91): 92,
        ('MELBOURNE                      UC501', 1171, 126): 127,
        ('MELBOURNE                      UC501', 1172, 116): 117,
        ('MELBOURNE                      UC501', 1173, 161): 162,
        ('MELBOURNE                      UC501', 1174, 166): 167,
    },
    17: {},
}

