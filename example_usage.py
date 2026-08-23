from client import MultiAgentTaskAuctionBiddingOrchestratorClient

def main():
    client = MultiAgentTaskAuctionBiddingOrchestratorClient()
    res = client.run_auction({'task_id': 'tsk_code_audit', 'required_caps': ['STATIC_ANALYSIS']})
    print('Auction Status: ' + res['auction_status'] + ' -> Winner: ' + res['winning_agent'] + ' (' + str(res['auction_latency_ms']) + 'ms)')
    print('Bids Evaluated:')
    for b in res['bids_received']:
        print('  [' + b['status'] + '] ' + b['agent_id'] + ' (Score: ' + str(b['bid_score']) + ', Cost: $' + str(b['cost_usd']) + ')')

if __name__ == '__main__':
    main()
