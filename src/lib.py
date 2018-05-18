DECODING_FAILED = "Decoding failed."
DECODING_NOT_READY = "Decoding not ready."

# Encodings
UTF_8 = "utf-8"
LATIN_1 = "latin1"
UNICODE_ESCAPE = "unicode_escape"

# Paths
FILENAME_READ = "input.txt"
FILENAME_WRITE = "output.txt"

# Encoder
BYTE_ENDIANESS = "big"
BYTE_BIT_SIZE = 8
BYTE_DIFF_VALUES = 256
BIG_PRIME_NUMBER = 32416190071
CODE_WORD_LENGTH = int(255 / 51)
MESSAGE_LENGTH = 180  # MODIFIABLE
CHUNK_SIZE = 1  # MODIFIABLE
NEEDED_AMOUNT_OF_VECTORS = (
    CODE_WORD_LENGTH * int(BYTE_BIT_SIZE / CHUNK_SIZE))

BYTE_RANGE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
              28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
              53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
              79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103,
              104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124,
              125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
              146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166,
              167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187,
              188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208,
              209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229,
              230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250,
              251, 252, 253, 254, 255]
BYTE_RANGE_RANDOMIZED = [119, 238, 101, 220, 83, 202, 65, 184, 47, 166, 29, 148, 11, 130, 249, 112, 231, 94, 213, 76,
                         195, 58, 177, 40, 159, 22, 141, 4, 123, 242, 105, 224, 87, 206, 69, 188, 51, 170, 33, 152,
                         15, 134, 253, 116, 235, 98, 217, 80, 199, 62, 181, 44, 163, 26, 145, 8, 127, 246, 109, 228,
                         91, 210, 73, 192, 55, 174, 37, 156, 19, 138, 1, 120, 239, 102, 221, 84, 203, 66, 185, 48,
                         167, 30, 149, 12, 131, 250, 113, 232, 95, 214, 77, 196, 59, 178, 41, 160, 23, 142, 5, 124,
                         243, 106, 225, 88, 207, 70, 189, 52, 171, 34, 153, 16, 135, 254, 117, 236, 99, 218, 81, 200,
                         63, 182, 45, 164, 27, 146, 9, 128, 247, 110, 229, 92, 211, 74, 193, 56, 175, 38, 157, 20,
                         139, 2, 121, 240, 103, 222, 85, 204, 67, 186, 49, 168, 31, 150, 13, 132, 251, 114, 233, 96,
                         215, 78, 197, 60, 179, 42, 161, 24, 143, 6, 125, 244, 107, 226, 89, 208, 71, 190, 53, 172,
                         35, 154, 17, 136, 255, 118, 237, 100, 219, 82, 201, 64, 183, 46, 165, 28, 147, 10, 129, 248,
                         111, 230, 93, 212, 75, 194, 57, 176, 39, 158, 21, 140, 3, 122, 241, 104, 223, 86, 205, 68,
                         187, 50, 169, 32, 151, 14, 133, 252, 115, 234, 97, 216, 79, 198, 61, 180, 43, 162, 25, 144,
                         7, 126, 245, 108, 227, 90, 209, 72, 191, 54, 173, 36, 155, 18, 137, 0]
BYTE_RANDOMIZE_MAP = dict(zip(BYTE_RANGE, BYTE_RANGE_RANDOMIZED))
BYTE_RECOVER_MAP = dict(zip(BYTE_RANGE_RANDOMIZED, BYTE_RANGE))

# Samples and Time
SAMPLES_PER_SEC = 6000
TIME_PER_CHUNK = 1  # MODIFIABLE
TOTAL_ELEM_NUMBER = NEEDED_AMOUNT_OF_VECTORS * TIME_PER_CHUNK
ELEMENTS_PER_CHUNK = int(TIME_PER_CHUNK * SAMPLES_PER_SEC)
RECORDING_TIME_IN_ADDITION = 5  # MODIFIABLE
NOISE_TIME = 2  # MODIFIABLE
RECORDING_TIME_TOTAL = NEEDED_AMOUNT_OF_VECTORS * TIME_PER_CHUNK + \
    NOISE_TIME + RECORDING_TIME_IN_ADDITION
RECORDING_SAMPLES_TOTAL = RECORDING_TIME_TOTAL * SAMPLES_PER_SEC
NUMBER_DATA_SAMPLES = int(SAMPLES_PER_SEC * TOTAL_ELEM_NUMBER)

# Noise Generation
FREE_FREQ_MIN = 1000
FREE_FREQ_MAX = 2000
LOWER_LOW_FREQUENCY_BOUND = 1000
LOWER_UPPER_FREQUENCY_BOUND = 2000
UPPER_LOW_FREQUENCY_BOUND = 2000
UPPER_UPPER_FREQUENCY_BOUND = 3000
NOISE_FREE_BANDWIDTH = 1000
FREQUENCY_STEP = NOISE_FREE_BANDWIDTH / (CHUNK_SIZE + 1)
NOISE_AMPLIFIER = 100  # MODIFIABLE
NOISE_DETECTION_TIME = 2  # MODIFIABLE
NUMBER_NOISE_SAMPLES = int(SAMPLES_PER_SEC * NOISE_TIME)
NOISE_SEED = 42
