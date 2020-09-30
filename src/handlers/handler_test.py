from . import handler
from os import environ


def test_my_handler_happy_path(mocker):
    # given
    table_name = 'test_table'
    log_name = 'test_log_stream'
    context = mocker.Mock(log_stream_name=log_name)
    environ['DDB_TABLE'] = table_name
    mock_client = mocker.Mock()
    mock_table = mocker.Mock()
    handler.dynamodb = mock_client
    mock_client.Table.return_value = mock_table
    mock_table.update_item.return_value = {}

    # when
    result = handler.my_handler(None, context)

    # then
    mock_client.Table.assert_called_with(table_name)
    mock_table.update_item.assert_called_once()
    kwargs = mock_table.update_item.call_args.kwargs
    assert kwargs['Key'] == {'id': log_name}
    assert result == {'body': 'Hello from Lambda3!'}
