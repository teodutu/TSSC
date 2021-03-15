#include "string.h"
#include "Enclave_t.h"
#include <stdio.h>
#include <cstdint>

/* TODO: Add SGX trusted libraries headers if needed */
#include <sgx_trts.h>
#include <sgx_tseal.h>

#define SECRET_FILE "enclave_secret"

void printf(const char *fmt, ...)
{
    char buf[BUFSIZ] = {'\0'};
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(buf, BUFSIZ, fmt, ap);
    va_end(ap);
    ocall_print(buf);
}

int get_sum(int a, int b)
{
	ocall_print("Adding numbers inside enclave...");
	return a + b;
}

/* TODO 1: Generate a random unsigned int using a trusted library */
unsigned int generate_random_number()
{
	// Add code here
	uint32_t rand;
	sgx_status_t status = sgx_read_rand((unsigned char*)&rand, sizeof(rand));
	if (SGX_SUCCESS != status)
		return 0;

	return rand;
}


/* TODO 3: Sealing function */
void seal_secret()
{
	// Add code here to seal "SGX_RULLZ".
	// TODO 4: Generate random string to seal.
	sgx_status_t status;
	unsigned char buf[64];
	uint32_t cipher_len = sgx_calc_sealed_data_size(0, sizeof(buf));
	sgx_sealed_data_t* sealed;
	size_t i;

	status = sgx_read_rand(buf, sizeof(buf));
	if (SGX_SUCCESS != status)
		return;

	sealed = (sgx_sealed_data_t*)malloc(cipher_len);
	if (!sealed)
		return;

	status = sgx_seal_data(
		0,
		NULL,
		sizeof(buf),
		buf,
		cipher_len,
		sealed
	);
	if (SGX_SUCCESS != status)
		return;

	ocall_write_file(SECRET_FILE, (char *)sealed, cipher_len);
	free(sealed);

	printf("Encrypted text: ");
	for (i = 0; i != sizeof(buf); ++i)
		printf("0x%X ", buf[i] & 0xff);
	printf("\n");
}


/* TODO 5: Unsealing function */
void unseal_secret()
{
	// Add code here
	static char encrypted[1024], decrypted[1024];
	sgx_status_t status;
	uint32_t len, i;

	ocall_read_file(SECRET_FILE, encrypted, sizeof(encrypted));

	status = sgx_unseal_data(
		(sgx_sealed_data_t*)encrypted,
		NULL,
		0,
		(uint8_t*)decrypted,
		&len
	);
	if (SGX_SUCCESS != status)
		return;
	
	printf("Decrypted text: ");
	for (i = 0; i != len; ++i)
		printf("0x%X ", decrypted[i] & 0xff);
	printf("\n");
}
