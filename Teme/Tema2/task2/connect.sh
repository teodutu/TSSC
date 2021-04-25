#!/bin/bash
# OpenSSH-based web tunnelling script.

SSHKEY="${1:-id_rsa}"
LOCAL_PORT=8080
DEST=catz@isc2021.root.sx
SOCKET=/tmp/catsshsocket

function cleanup() {
	[[ ! -f "$SOCKET" ]] || \ 
		ssh -S "$SOCKET" -O exit "$DEST" >/dev/null 2>&1 || true
}
trap cleanup EXIT

set -e

ssh -M -S "$SOCKET" -i "$SSHKEY" -fNnT "$DEST"
ssh -S "$SOCKET" -O check "$DEST"

ALLOCATED_PORT=$(ssh -S "$SOCKET" "$DEST" get-forward-port)
if [[ -z "$ALLOCATED_PORT" ]]; then
	exit 1
fi
echo "Allocated server port: $ALLOCATED_PORT"
ssh -S "$SOCKET" -O forward -o "ExitOnForwardFailure=yes" -L "$LOCAL_PORT:localhost:$ALLOCATED_PORT" "$DEST"

ssh -S "$SOCKET" "$DEST" start

