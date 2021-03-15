#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

#include "Enclave_u.h"
#include "sgx_urts.h"
#include "sgx_utils/sgx_utils.h"

/* Global Enclave ID */
sgx_enclave_id_t global_eid;

/* OCall implementations */
void ocall_print(const char* str)
{
	printf("%s\n", str);
}

void ocall_write_file(const char* filename, const char* buf, size_t buf_len)
{
	/* TODO 2: Implement write */
	ssize_t bytes_written, total_written = 0;
	int fd = open(filename, O_WRONLY | O_CREAT, 0644);
	if (fd < 0) {
		perror("open failed");
		return;
	}

	do {
		bytes_written = write(fd, buf + total_written, buf_len);
		if (bytes_written < 0) {
			perror("write failed");
			break;
		}

		total_written += bytes_written;
		buf_len -= bytes_written;
	} while (buf_len);

	close(fd);
}

void ocall_read_file(const char* filename, char* buf, size_t buf_len)
{
	/* TODO 2: Implement write */
	ssize_t bytes_read, total_read = 0;
	int fd = open(filename, O_RDONLY);
	if (fd < 0) {
		perror("open failed");
		return;
	}

	do {
		bytes_read = read(fd, buf + total_read, buf_len);
		if (bytes_read < 0) {
			perror("read failed");
			break;
		}
		if (!bytes_read)
			break;

		total_read += bytes_read;
		buf_len -= bytes_read;
	} while (buf_len);

	close(fd);	
}

int main(void)
{
	int sum_result;
	uint rand = 1;
	sgx_status_t status;
	char buf[16];
  
	/* Enclave Initialization */ 
	if (initialize_enclave(&global_eid, "enclave.token", "enclave.signed.so") < 0) {
		printf("Fail to initialize enclave.\n");
		return 1;
	}

	/* Call a simple method inside enclave */ 
	status = get_sum(global_eid, &sum_result, 3, 4);
	if (status != SGX_SUCCESS) {
		printf("ECall failed.\n");
		return 1;
	}
	printf("Sum from enclave: %d\n", sum_result);
	
	/* TODO 1: Using an ECALL that generates a random unsigned int,
	get a random number between 3 and 42. */ 
	status = generate_random_number(global_eid, &rand);
	if (SGX_SUCCESS != status) {
		printf(
			"ECall generate_random_number failed with status 0x%X\n",
			status
		);
		return 1;
	}
	rand = rand % 40 + 3;
	printf("random number = %u\n", rand);

	ocall_write_file("gigel.txt", "valoare!\n", 10);
	ocall_read_file("gigel.txt", buf, 10);
	printf("file contains: %s", buf);

	/* TODO 3, TODO 4: Uncomment sealing/unsealing calls */ 
	status = seal_secret(global_eid);
	if (SGX_SUCCESS != status) {
		printf("ECall seal_secret failed with status 0x%X\n", status);
		return 1;
	}

	status = unseal_secret(global_eid);
	if (SGX_SUCCESS != status) {
		printf("ECall unseal_secret failed with status 0x%X\n", status);
		return 1;
	}

	return 0;
}
