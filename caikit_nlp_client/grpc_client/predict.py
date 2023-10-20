from prediction_service import PredictionServiceStub
import argparse
import grpc
from client_utils import prepare_certs


def main():
    parser = argparse.ArgumentParser(
        description='Client library for Caikit-TGIS to call prediction')

    parser.add_argument('--input_text', required=True, help='Input text on which prediction needs to be run')
    parser.add_argument('--grpc_address', required=False, default='localhost',
                        help='Specify url to grpc service. default:localhost')
    parser.add_argument('--grpc_port', required=False, default=8085, help='Specify port to grpc service. default: 8085')
    parser.add_argument('--model_id', required=True, default='face-detection', help='Specify the model name')
    parser.add_argument('--tls', default=False, action='store_true', help='use TLS communication with gRPC endpoint')
    parser.add_argument('--server_cert', required=False, help='Path to server certificate')
    parser.add_argument('--client_cert', required=False, help='Path to client certificate')
    parser.add_argument('--client_key', required=False, help='Path to client key')
    args = vars(parser.parse_args())

    address = "{}:{}".format(args['grpc_address'], args['grpc_port'])

    if args.get('tls'):
        server_ca_cert, client_key, client_cert = prepare_certs(server_cert=args['server_cert'],
                                                                client_key=args['client_key'],
                                                                client_ca=args['client_cert'])
        creds = grpc.ssl_channel_credentials(root_certificates=server_ca_cert,
                                             private_key=client_key, certificate_chain=client_cert)
        channel = grpc.secure_channel(address, creds)
    else:
        channel = grpc.insecure_channel(address)

    stub = PredictionServiceStub(channel)

    input_text = args['input_text']
    print("input_text : ", input_text)

    model_id = args['model_id']
    print("model_id : ", model_id)
    metadata = [("mm-model-id", model_id)]

    request = stub.TextGenerationTaskRequest
    request.text = input_text
    request.preserve_input_text = False
    request.max_new_tokens = 200
    request.min_new_tokens = 10

    response = stub.TextGenerationTaskPredict(
        request=request,
        metadata=metadata
    )
    print("Response :", response.generated_text)


if __name__ == "__main__":
    main()
