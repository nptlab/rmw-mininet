from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import set_ev_cls, CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.ofproto import ofproto_v1_0


class Controller(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)

    # def _add_flow(self, datapath, priority, match, actions):
    #     ofproto = datapath.ofproto
    #     parser = datapath.ofproto_parser
    #
    #     flow_mod_msg = parser.OFPFlowMod(datapath=datapath,
    #                             priority=priority,
    #                             match=match,
    #                             actions=actions)
    #     datapath.send_msg(flow_mod_msg)


    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        msg = ev.msg
        #self.logger.info(msg)
        self.logger.info('OFPSwitchFeatures received: '
                          'datapath_id=0x%016x n_buffers=%d '
                          'n_tables=%d n_ports=%d'
                          'capabilities=0x%08x',
                          msg.datapath_id, msg.n_buffers, msg.n_tables,
                          len(msg.ports) , msg.capabilities)

        self.logger.info('Install table-miss flow entry: send to controller if no rule is fired')
        datapath = msg.datapath
        ofproto = datapath.ofproto # modulo OpenFlow protocol della versione corrispondente a quella negoziata
        self.logger.info(ofproto)
        parser = datapath.ofproto_parser

        match_part = parser.OFPMatch() # Match vuoto perche' e' la regola ti table-miss
        actions_part = [ parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, 65509  ) ]

        # Inviamo allo switch un messaggio FlowMod per modificare la flow-table
        # costruzione del messaggio

        flow_priority = 0 # La piu' bassa possibile

        flow_mod_msg = parser.OFPFlowMod(datapath=datapath,
                                         priority= flow_priority,
                                         match=match_part,
                                         actions=actions_part)

        # invio del messaggio allo switch corrispondente
        datapath.send_msg(flow_mod_msg)

    # @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    # def packet_in_handler(self, ev):
    #     msg = ev.msg
    #     datapath = msg.datapath
    #     ofproto = datapath.ofproto
    #     parser = datapath.ofproto_parser
    #
    #     # analyse the received packets using the packet library.
    #     pkt = packet.Packet(msg.data)
    #     eth_pkt = pkt.get_protocol(ethernet.ethernet)
    #     dst = eth_pkt.dst
    #     src = eth_pkt.src
    #
    #     # get the received port number from packet_in message.
    #     in_port = msg.in_port
    #
    #     self.logger.info("packet in %s %s", datapath.id,  pkt)







