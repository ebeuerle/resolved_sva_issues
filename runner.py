#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lib

class HaloSVA_issues():
    def __init__(self):
        self.output = [["Server Hostname", "Server FQDN", "Primary IP address"]]
        config = lib.ConfigHelper()
        self.sva = lib.ServerController(config)
        self.list_sva = []

    def build(self):
        self.list_sva = self.sva.get_sva_issues()

    def run(self):
        self.build()
        for server in self.list_sva:
            self.output.append([server["hostname"], server["reported_fqdn"], server["primary_ip_address"]])
        lib.CsvWriter.write(self.output)

def main():
    halo_sva_issues = HaloSVA_issues()
    halo_sva_issues.run()

if __name__ == "__main__":
    main()
