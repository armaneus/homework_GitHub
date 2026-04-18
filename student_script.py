import ROOT
h = ROOT.TH1F("h", "Homework Histogram", 100, 0, 10)
for i in range(1000):
h.Fill(ROOT.gRandom.Gaus(5, 3))
print("Entries=", h.GetEntries())
EOF

